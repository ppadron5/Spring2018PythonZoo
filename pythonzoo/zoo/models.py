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
	
	def __str__ (self):
		return self.name		

class Animal(models.Model):
	name = models.CharField(max_length=200, help_text="Enter an Exhibit Name)")
	imageFileName = models.CharField(max_length=200, help_text="Enter Image", null=True)
	exhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
	soundFileName = models.CharField(max_length=200, help_text="Enter Sound File", null=True, blank=True)
	habitatDescription = models.TextField(max_length=1000, help_text="Enter Habitat Description")
	
	def __str__ (self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('animalDetail', args=[str(self.id)])
		
class ExhibitNeighor(models.Model):
	fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='fromExhibit')
	toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='toExhibit')
	CARDINAL = (
		('n', 'North'),
		('s', 'South'),
		('e', 'East'),
		('w', 'West'),
		('sw', 'SouthWest'),
		('se', 'SouthEast'),
		('ne', 'NorthEast'),
		('nw', 'NorthWest')
	)
	direction= models.CharField(max_length=2, choices=CARDINAL, help_text="Enter Direction", null=True, blank=True)

