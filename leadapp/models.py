from django.db import models


# Create your models here.


class LEAD(models.Model):

    name=models.CharField(max_length=50)

    email=models.EmailField()

    phone_number=models.CharField(max_length=14)

    STATUS_CHOICES=(


        ('new','new'),
        ('in_progress','in_progress'),
        ('converted','converted'),
        ('rejected','rejected'),
    )

    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default="new")


    SOURCE_CHOICES=(

        ('online','online'),
        ('referral','referral'),
        ('event','event'),
        ('advertisement','advertisement'),
    )

    source=models.CharField(max_length=100,choices=SOURCE_CHOICES,default="online")

    def _str_(self):
        return self.name

        