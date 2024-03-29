from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # new method
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # old method
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    res = f'You\'re looking at the results of question {question_id}.'
    return HttpResponse(res)


def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}.')


def owner(request):
    return HttpResponse("Hello, world. 2fe10492 is the polls index.")
