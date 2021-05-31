from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Todo(models.Model):
    NEW = 'new'
    FINISHED = 'finished'
    STATUS = [
        (NEW, 'new'),
        (FINISHED, 'finished')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=512)
    status = models.CharField(choices=STATUS, max_length=10, default=NEW)

    def mark_as_finished(self):
        self.status = self.FINISHED
        self.save()

    def mark_as_unfinished(self):
        self.status = self.NEW
        self.save()
