from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Breed, Cat
# Create your views here.

# main room


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        breed_count = Breed.objects.all().count()
        all_cats = Cat.objects.all()

        cat_info = {'breed_count': breed_count, 'all_cats': all_cats}
        return render(request, 'cats/cats_list.html', cat_info)

# making a new breed


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all()

        breed_info = {'breed_list': breed_list}
        return render(request, 'cats/breed_list.html', breed_info)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
