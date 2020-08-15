from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question
# Create your views here.

from django.http import HttpResponse
from polls.forms import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'index.html', context)
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question =get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html',{'question': question})

def vote(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoseNotExist):

        return render(request, 'detail.html',{
            'question':question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('results',args=(question.id,)))



# def write(request):
#     if request.method =='post' :
#         form =Form(request.POST)
#         if form.is_valid:
#             form.save()

#     else:
#         form = Form()
#     return render(request, 'write.html', {'form':form})


# def list(request):
#     questionList =Question.objects.all()
#     return render(request, 'list.html', {'questionList':questionList})
