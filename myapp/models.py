from django.db import models
# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=30,verbose_name='Enter Name')
    phone = models.IntegerField(verbose_name='Enter Mobile Number',help_text='Mobile number should contain 10 digits')
    mailid = models.EmailField(verbose_name='Enter Mail id')
    course = models.CharField(max_length=20,choices=[
        ('Java','Java'),
        ('Python','Python3'),
        ('C','C'),
        ('C++','C++'),
        ('Django','Django')
    ],default='Others')

class Student(models.Model):
    stdId = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=30)
    mail = models.EmailField()
    mobile = models.IntegerField()
    course = models.CharField(max_length=20,choices=[
        ('Python','Python'),
        ('Java','Java'),
        ('C','C'),
        ('C++','C++'),
        ('Django','Django'),
        ('Full Stack','Full Stack')
    ])
    fees = models.IntegerField()
    status = models.CharField(max_length=15,choices=[
        ('Completed','Completed'),
        ('Ongoing','Ongoing'),
        ('Yet to Start','Yet to Start'),
        ('Hold','Hold'),
        ('Discontinued','Discontinued')
    ])
    date = models.DateField()

