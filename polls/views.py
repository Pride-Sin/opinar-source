# Django imports
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Local imports
from .models import Poll, PollVote, Vote as NewVote
from .forms import PollForm, VoteForm


class PollList(LoginRequiredMixin, ListView):
    model = Poll
    context_object_name = 'polls'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['polls'] = context['polls'].filter(user=self.request.user)
        return context

class PollDetail(DetailView):
    model = Poll
    context_object_name = 'poll'

class PollCreate(LoginRequiredMixin, CreateView):
    model = Poll
    form_class = PollForm
    #fields = ['question', 'allow_anon', 'allow_comments', 'allow_result']
    success_url = reverse_lazy('polls')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PollCreate, self).form_valid(form)

class PollUpdate(LoginRequiredMixin, UpdateView):
    model = Poll
    form_class = PollForm
    #fields = ['question', 'allow_anon', 'allow_comments', 'allow_result']
    success_url = reverse_lazy('polls')

class PollDelete(LoginRequiredMixin, DeleteView):
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('polls')


def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    user = request.user

    if 'user_vote' in request.POST:
        # Result of the vote in form
        user_vote = request.POST['user_vote']

        if user_vote == 'true':
            user_vote = True
        else:
            user_vote = False

        # Create the vote 
        new_vote, vote_created = NewVote.objects.get_or_create(user=user, vote=user_vote)


    context = {'poll' : poll, 'user' : user}
    return render(request, 'vote.html', context=context)