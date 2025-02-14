from django.db import models

# Create your models here.
class QuestionPaper(models.Model):
    subject=models.CharField(primary_key=True, max_length=100)
    qno=models.IntegerField()
    ques=models.CharField(max_length=500)