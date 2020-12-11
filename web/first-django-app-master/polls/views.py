from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Question

### Create your views here. ###

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return last five questions
        return Question.objects.filter(
            pub_date__lte = timezone.now()        
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# Voting view
def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Use F function avoiding race conditions
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


## default indexex
#def index(request):
#    #return HttpResponse("Hello, world. polls index");
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    ### HttpResponse ver. ###
#    # template = loader.get_template('polls/index.html')
#    # return HttpResponse(template.render(context, request))
#    ### Shortcuts ver. ###
#    return render(request, 'polls/index.html', context)

## Question view
#def detail(request, question_id):
#    ### Http404 ver. ###
#    # try:
#    #    question = Question.objects.get(pk=question_id)
#    # except Question.DoesNotExist:
#    #    raise Http404("Question does not exist")
#    ### get_object_or_404, get_list_or_404 ver. ###
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})

## Result View 
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})


