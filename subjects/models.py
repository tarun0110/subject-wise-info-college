from django.db import models
import datetime
# Create your models here.
from django.utils import timezone


class Subjects(models.Model):
    subjects_text = models.CharField(max_length=50)

    def __str__(self):
        return self.subjects_text


class Syllabus(models.Model):
    sub_syl = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    syllabus_text = models.CharField(max_length=500)

    def __str__(self):
        return self.syllabus_text


class Topics_today(models.Model):
    sub_syl2= models.ForeignKey(Subjects, on_delete= models.CASCADE)
    topics_today_text=models.CharField(max_length=500)
    date_today=models.DateTimeField('date published')
    def __str__(self):
        return self.topic_today_text
