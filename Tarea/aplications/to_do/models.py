from django.db import models
from aplications.users.models import User

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.title



