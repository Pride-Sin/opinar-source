# Django imports
from django.db import models
# Local imports
from users import models as userModels


# Create your models here.
class Poll(models.Model):
    user = models.ForeignKey(userModels.User, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=60)
    allow_anon = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=False)
    allow_result = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "polls"


# Choices for vote
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
class Vote(models.Model):
    user = models.ForeignKey(userModels.User, on_delete=models.SET_NULL, null=True)
    vote = models.BooleanField(choices=BOOL_CHOICES)


class PollVote(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.SET_NULL, blank=True, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        name = self.poll.question + ' ' + '(' + str(self.vote.user.pk) + ')'
        return name