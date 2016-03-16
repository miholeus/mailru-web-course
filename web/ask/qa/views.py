from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Question, Answer

def index(request, *args, **kwargs):
    posts = Question.objects.all()
    page = request.GET.get('page') or 1
    try:
        page = int(page)
    except:
        page = 1
    if page < 1:
        page = 1
    limit = 10
    posts = posts[(page-1)*limit:limit]
    return render(request, 'index.html', {'post_list':posts})

def popular(request, *args, **kwargs):
    posts = Question.objects.all()
    posts = posts.order_by('-rating')
    page = request.GET.get('page') or 1
    try:
        page = int(page)
    except:
        page = 1
    if page < 1:
        page = 1
    limit = 10
    posts = posts[(page-1)*limit:limit]
    return render(request, 'popular.html', {'post_list':posts})

def question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        answers = Answer.objects.all()
        answers = answers.filter(question=question)
        answers = answers.order_by('-added_at')
        return render(request, 'question.html', {'question':question, 'answers':answers})
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h1>Question not Found</h1>")

def test(request, *args, **kwargs):
    return HttpResponse("OK")

def not_found(request, *args, **kwargs):
    return HttpResponseNotFound("<h1>Page not Found</h1>")
