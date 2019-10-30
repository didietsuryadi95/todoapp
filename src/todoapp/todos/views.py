from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic.base import View

from .forms import TodoForm
from .models import Todo

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template('home.html')
        todos = Todo.objects.all()
        context = {
            'todos': todos,
            'form': TodoForm,
        }
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        data = request.POST
        Todo.objects.create(content=data.get('content'), status=data.get('status'))
        template = loader.get_template('home.html')
        todos = Todo.objects.all()
        context = {
            'todos': todos,
            'form': TodoForm,
        }
        return HttpResponse(template.render(context, request))


class LogoutView(TemplateView):
    template_name = 'registration/logout.html'