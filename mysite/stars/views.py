from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Star, Type
# Create your views here.


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        type_count = Type.objects.all().count()
        stars = Star.objects.all()

        stars_info = {'type_count': type_count, 'star_list': stars}
        return render(request, 'stars/stars_list.html', stars_info)


class TypeView(LoginRequiredMixin, View):
    def get(self, request, *args):
        types = Type.objects.all()
        types_info = {'type_list': types}
        return render(request, 'stars/type_list.html', types_info)


class StarCreate(LoginRequiredMixin, CreateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


class StarDelete(LoginRequiredMixin, DeleteView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


class TypeCreate(LoginRequiredMixin, CreateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')
