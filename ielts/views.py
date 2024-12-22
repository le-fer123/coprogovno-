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
I am a developer and I want to use you as a methodologist for the IELTS oral interview. I will provide you with the criteria, user audio, and the text of the interview itself.

You are required to:

Evaluate each part of the test according to the IELTS band descriptors.
Offer recommendations and advice for improvement.
Provide an overall band score.
Please ensure your explanations are clear and understandable. Your response will be broadcast to the user, so tailor your answer as if speaking directly to a client.

Format:

Add a score at the start of each part, followed by the final score.
Clearly explain the reasoning for the scores and provide actionable advice.
There is a dialogue history included here. Use it to maintain context when answering the user’s latest question. If there is no specific question, answer based on the provided context.

Also, use moderation. if the user's prompt is illogical or it is not clear what he means, write to him directly
Also add emojies, many emojies

IELTS Band Descriptors:

Band 9: Expert user – Full operational command of English; fluent, accurate, and shows complete understanding.
Band 8: Very good user – Fully operational command with occasional inaccuracies; handles complex arguments well.
Band 7: Good user – Generally effective command; occasional errors; handles complex reasoning.
Band 6: Competent user – Effective command despite inaccuracies; manages fairly complex language.
Band 5: Modest user – Partial command; many mistakes but copes with overall meaning.
Band 4: Limited user – Basic competence in familiar situations; struggles with complex language.
Band 3: Extremely limited user – Understands general meaning only in very familiar situations.
Band 2: Intermittent user – Great difficulty understanding spoken/written English.
Band 1: Non-user – No ability except a few isolated words.
Band 0: Did not attempt the test.
IELTS TEST:

            '''
        context += '\n\n' + sample.first.content
        context += '\n\n' + sample.second.content
        context += '\n\n' + sample.second.followup
        context += '\n\n' + sample.third.content
        context += '\n\n' + "THIS IS A HISTORY OF CHAT:"

        print(context)
        try:
            result, content = answer_gen(audio_path, context)
        except ssl.SSLError as e:
            return JsonResponse({"error": f"SSL Error: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

        return JsonResponse({"message": "ZAEBIS", "content": content, "context": context, "sample_id": sample.id})
@method_decorator(csrf_exempt, name='dispatch')
class QuestionView(View):
    def post(self, request, *args, **kwargs):
        audio_file = request.FILES.get('audio')
        context = request.POST.get("context")

        audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', audio_file.name)
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        with open(audio_path, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)

        result, content = answer_gen(audio_path, context)

        return JsonResponse({"message": "ZAEBIS", "content": content, "audio": audio_path, "context": context})



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
