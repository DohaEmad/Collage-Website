from django.db import models
from statistics import mode
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50,blank=True)
    id = models.CharField(max_length=8, primary_key=True,default='0', blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True)
    phone = models.CharField(max_length=11,blank=True)
    mail = models.CharField(max_length=50,blank=True)
    birthday = models.DateField(blank=True)

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(
        choices=GENDER,
        max_length=6,
        default='Female',
        blank=True,
    )
    STATE = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    state = models.CharField(
        choices=STATE,
        max_length=8,
        default='Active',
        blank=True
    )

    LEVEL = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),

    ]
    level = models.CharField(
        max_length=1,
        choices=LEVEL,
        default='1',
        blank=True
    )
    DEPARRMENT = [
        ('General', 'General'),
        ('CS', 'CS'),
        ('DS', 'DS'),
        ('AI', 'AI'),
        ('IS', 'IS'),
        ('IT', 'IT'),


    ]
    department = models.CharField(
        max_length=8,
        choices=DEPARRMENT,
        default='General',
        blank=True
    )
    def __str__(self):
        return self.id
    class Meta:
        ordering=['id']







