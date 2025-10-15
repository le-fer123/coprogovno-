from django.http import JsonResponse
import google.generativeai as genai

from .models import Sample


def get_sample(id):
    return Sample.objects.get(id=id)


def get_first_part(id_sample):
    sample = Sample.objects.get(id=id_sample)
    first_part = sample.first_part

    return first_part


def get_second_part(id_sample):
    sample = Sample.objects.get(id=id_sample)
    second_part = sample.second_part

    return second_part


def get_third_part(id_sample):
    sample = Sample.objects.get(id=id_sample)
    third_part = sample.third_part

    return third_part


def validation_answer(audio_file, sample_id):
    if not audio_file or not sample_id:
        return JsonResponse({"error": "Both 'audio' and 'sample_id' are required."}, status=400)


def answer_gen(audio, context):
    genai.configure(api_key="AIzaSyBJ7l-knz2iWlt9n68Cc_BUyLi77iOcPD8")

    audio = genai.upload_file(path=audio)
    print(f"{audio=}")

    model = genai.GenerativeModel("gemini-2.5-flash")
    result = model.generate_content([audio, context])
    text = result.text

    return result, text


def question_get(context):
    genai.configure(api_key="AIzaSyBJ7l-knz2iWlt9n68Cc_BUyLi77iOcPD8")

    model = genai.GenerativeModel("gemini-2.5-flash")
    result = model.generate_content([context])
    text = result.text

    return result, text
