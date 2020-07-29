from django.db import models

class todoList(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


