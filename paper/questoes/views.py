from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

def index(request):
    return HttpResponse("PAPER")

def detail(request, question_id):
    return HttpResponse("Essa é a questão %s." % question_id)

def resultados(request, question_id):
    response = "Resultados da questão (verificar utilidade) %s."
    return HttpResponse(response % question_id)

def resposta(request, question_id):
    return HttpResponse("Você está respondendo a questão %s." % question_id)

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questoes/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("A questão não existe")
    return render(request, 'questoes/detail.html', {'question': question})

# Create your views here.
