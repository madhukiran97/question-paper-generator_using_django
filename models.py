from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.forms import ModelForm
# Create your models here.
SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)
COURSE_CHOICES = (
    ("MCA", "MCA"),
    ("MBA", "MBA"),
    ("MCOM", "MCOM"),
    ("MSC", "MSC"),    
    
)
class subject(models.Model):
    course=CharField(max_length=10,choices=COURSE_CHOICES,default='MCA')
    sub_code=IntegerField(primary_key=True)
    sem=CharField(max_length=10,choices=SEMESTER_CHOICES,default='1')
    subject=TextField()
TYPE_CHOICE=(
    ("short","short"),
    ("long","long"),
) 
UNIT_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5","5"))   
class questions(models.Model):
    course=CharField(max_length=10,choices=COURSE_CHOICES,default='MCA')
    sem=IntegerField(choices=SEMESTER_CHOICES,default='1')
    sub_code=IntegerField()
    type=CharField(max_length=10,choices=TYPE_CHOICE,default='short')
    unit=IntegerField(choices=UNIT_CHOICES,default='1')
    question=TextField()
class objective_questions(models.Model):
    course=CharField(max_length=10,choices=COURSE_CHOICES,default='MCA')
    sem=IntegerField(choices=SEMESTER_CHOICES,default='1')
    sub_code=IntegerField()
    unit=IntegerField(choices=UNIT_CHOICES,default='1')
    question=TextField()
    option1=TextField()
    option2=TextField()
    option3=TextField()
    option4=TextField()
    answer=TextField()

    
    
    
