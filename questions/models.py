from django.db import models
from category.models import Category

# Create your models here.

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    text = models.TextField()
    explanation = models.TextField(blank=True, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)



    def __str__(self):
        return self.text


