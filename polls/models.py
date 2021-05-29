# Django imports
from django.db import models
# Local imports
from users import models as userModels


# Create your models here.
class Poll(models.Model):
    user = models.ForeignKey(userModels.User, on_delete=models.CASCADE)
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