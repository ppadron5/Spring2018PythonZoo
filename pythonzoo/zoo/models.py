# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.

class Zoo(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a Zoo Name)")
	logoFileName = models.CharField(max_length=200, help_text="Enter a Zoo Name)", null=True)
	
	def __str__ (self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('zooDetail', args[str(self.id)])
	
class Exhibit(models.Model):
	name = models.CharField(max_length=200, help_text="Enter an Exhibit Name)")
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
	
	def get_absolute_url(self):
		return reverse('exhibitDetail', args=[str(self.id)])
	
	def getZooName(self):
		return self.zoo.name	

