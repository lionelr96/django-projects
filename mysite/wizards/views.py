from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Wizard, House
# Create your views here.


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        hc = House.objects.all().count()
        wl = Wizard.objects.all()

        wtx = {'house_count': hc, 'wizard_list': wl}
        return render(request, 'wizards/wizards_list.html', wtx)


class HouseView(LoginRequiredMixin, View):
    def get(self, request):
        hl = House.objects.all()
        wtx = {'house_list': hl}
        return render(request, 'wizards/house_list.html', wtx)


class WizardCreate(LoginRequiredMixin, CreateView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')


class WizardUpdate(LoginRequiredMixin, UpdateView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')


class WizardDelete(LoginRequiredMixin, DeleteView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')


class HouseCreate(LoginRequiredMixin, CreateView):
    model = House
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')


class HouseUpdate(LoginRequiredMixin, UpdateView):
    model = House
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')


class HouseDelete(LoginRequiredMixin, DeleteView):
    model = House
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')
