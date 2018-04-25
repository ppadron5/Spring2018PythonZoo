# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Zoo(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a Zoo Name)")
	
	def __str__ (self):
		return self.name
	
class Exhibit(models.Model):
	name = models.CharField(max_length=200, help_text="Enter an Exhibit Name)")
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)	
