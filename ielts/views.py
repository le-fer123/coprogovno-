import ssl

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import os
from .serializers import *
from .services import *

@method_decorator(csrf_exempt, name='dispatch')
class AnswerUploadView(View):

    def post(self, request, *args, **kwargs):
        audio_file = request.FILES.get('audio')
        sample_id = int(request.POST.get('sample'))
        validation_answer(audio_file, sample_id)

        sample = Sample.objects.get(id=sample_id)

        audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', audio_file.name)
        print(audio_path)
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        with open(audio_path, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)
        context = \
            '''
            I am a developer and I want to use you as a methodologist for the ielts oral interview. I will provide you with the criteria, user audio and the text of the interview itself. You are required to evaluate each part of the test, offer recommendations, advice, and evaluate the overall score according to the ielts criteria set out below. please try to explain everything clearly and understandably
            Add a score at the head in the form of points in parts, and the final score
            Please keep in mind that your answer will be broadcast to the user, and not to me
            So answer as you should answer to a client
            
            Band 9	Expert user	You have a full operational command of the language. Your use of English is appropriate, accurate and fluent, and you show complete understanding.
            Band 8	Very good user	You have a fully operational command of the language with only occasional unsystematic inaccuracies and inappropriate usage. You may misunderstand some things in unfamiliar situations. You handle complex detailed argumentation well.
            Band 7	Good user	You have an operational command of the language, though with occasional inaccuracies, inappropriate usage and misunderstandings in some situations. Generally you handle complex language well and understand detailed reasoning.
            Band 6	Competent user	Generally you have an effective command of the language despite some inaccuracies, inappropriate usage and misunderstandings. You can use and understand fairly complex language, particularly in familiar situations.
            Band 5	Modest user	You have a partial command of the language, and cope with overall meaning in most situations, although you are likely to make many mistakes. You should be able to handle basic communication in your own field.
            Band 4	Limited user	Your basic competence is limited to familiar situations. You frequently show problems in understanding and expression. You are not able to use complex language.
            Band 3	Extremely limited user	You convey and understand only general meaning in very familiar situations. There are frequent breakdowns in communication.
            Band 2	Intermittent user	You have great difficulty understanding spoken and written English.
            Band 1	Non-user	You have no ability to use the language except a few isolated words.
            Band 0	Did not attempt the test	You did not answer the questions.'''
        context += '\n\n' + sample.first.content
        context += '\n\n' + sample.second.content
        context += '\n\n' + sample.third.content
        print(context)
        try:
            result, content = answer_gen(audio_path, context)
        except ssl.SSLError as e:
            return JsonResponse({"error": f"SSL Error: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

        return JsonResponse({"message": "ZAEBIS", "content": content, "sample_id": sample.id})


class FirstPartViewSet(viewsets.ModelViewSet):
    queryset = FirstPart.objects.all()
    serializer_class = FirstPartSerializer


class SecondPartViewSet(viewsets.ModelViewSet):
    queryset = FirstPart.objects.all()
    serializer_class = FirstPartSerializer


class ThirdPartViewSet(viewsets.ModelViewSet):
    queryset = ThirdPart.objects.all()
    serializer_class = ThirdPartSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = IELTSSampleSerializer
