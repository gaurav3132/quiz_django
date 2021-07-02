from django.db import models

# Create your models here.

class Paper(models.Model):
    question = models.CharField(max_length=50)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)