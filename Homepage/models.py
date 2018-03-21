# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Investor(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Username = models.CharField(max_length=100,default="")
    Contact = models.CharField(max_length=15,default="123456")
    City = models.CharField(max_length=20,default="Pune")
    Password = models.CharField(max_length=100)


