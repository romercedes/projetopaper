from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse
from .models import Question, Choice

def index(request): #Remover função?
    return HttpResponse("PAPER")

def detail(request, question_id):
    return HttpResponse("Essa é a questão %s." % question_id)

def resultados(request, question_id): # Aparentemente inútil, mas não retirar do código antes de identificar os vínculos
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questoes/resultados.html', {'question': question})

def resposta(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questoes/resultados.html', {'question': question})

def index(request):
    if request.method == "POST":
         Hab = request.POST.get('Hab', None)
    latest_question_list = Question.objects.all()
    context = {
        'latest_question_list': latest_question_list
        }
    return render(request, 'questoes/index.html', context)

def lista(request):
    if request.method == "POST":
         Hab = request.POST.get('Hab', None)
    filter_question_list = Question.objects.filter(habilidade=Hab)
    context = {
        'filter_question_list': filter_question_list
        }
    return render(request, 'questoes/lista.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("A questão não existe")
    return render(request, 'questoes/detail.html', {'question': question})

# Create your views here.
