from django.db import models

# Create your models here.
class Todos(models.Model):
    todo_id=models.CharField(max_length=100, default='your_default_value')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
