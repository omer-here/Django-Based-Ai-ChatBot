from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import openai

# from .models import Chat

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    answer = "I don't have credits"
    return answer


# Create your views here.
def home(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response })
    return render(request,'home.html')
    # return HttpResponse("This is Home Page!")
