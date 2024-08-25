import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from googletrans import Translator


def register(request):
    
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Conta criada para {username}!')
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})


@login_required
def random_joke(request):
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        joke = joke_data['value']
    else:
        joke = "Não foi possivel obter uma piada no momento."

    return render(request,'random_joke.html', {'joke':joke})

def get_joke(request):
    joke = random_joke()
    return render(request,'random_joke.html', {'joke':joke})

def translate_joke(request):
    if request.method == 'POST':
        joke = request.POST.get('joke')
        translator = Translator()
        translated = translator.translate(joke, dest='pt').text
        return render(request, 'random_joke.html', {'joke': translated})

    return redirect('get_joke')