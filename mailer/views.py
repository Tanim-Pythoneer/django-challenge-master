#-*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from django.core.paginator import Paginator

from mailer.models import Company



class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100

def mailer(request):
    all_task = model.objects.all()
    paginator = Paginator(all_task, 100)
    page = request.GET.get('page')
    all_task = paginator._get_page(page)
