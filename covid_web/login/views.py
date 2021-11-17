from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import User

class LoginView(generic.ListView):
    model = User
    template_name = 'login/login.html'

def auth(request):
    try:
        user = User.objects.get(userName=request.POST['username'])
    except (User.DoesNotExist):
        response = "User does not exists."
        return HttpResponse(response)
    else:
        response = "Name is " + user.userName + ". <br/>Password is " + user.password + "."
        return HttpResponse(response)



# class SuccessView(generic.SuccessView):
#     model = User
#     template_name = 'login/success.html'



# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))