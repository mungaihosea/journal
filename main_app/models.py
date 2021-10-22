from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    title = models.CharField(max_length= 300)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    last_edit = models.DateTimeField(null = True, blank=True)

    def __str__(self):
        return self.title
