from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
 
class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.title

class CoursesTaken(models.Model):
    SELECTION = ((11,'日曜日'),(12,'月曜日'),(13,'火曜日'),(14,'水曜日'),(15,'木曜日'),(16,'金曜日',),(17,'土曜日'))
    SELECTION1 = ((1,'１限'),(2,'2限'),(3,'3限'),(4,'4限'),(5,'5限'),(6,'6限'),(7,'7限'))
    name = models.CharField('履修科目名',max_length=255)
    CT_status = models.IntegerField('曜日',choices=SELECTION)
    period = models.IntegerField('時限',choices=SELECTION1)
    school_credit = models.IntegerField('単位数',default=0)
    
    def __str__(self):
        return self.name

