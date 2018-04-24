# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	temporaryData = "Bill"
	return render(
		request,
		"index.html",
		context = { 'temporaryData' : temporaryData }
    )
