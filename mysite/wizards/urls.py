from django.urls import path
from . import views

app_name = 'wizards'
urlpatterns = [
    path('', views.MainView.as_view(),name='all'),
    path('main/create/', views.WizardCreate.as_view(), name='wizard_create'),
    path('main/<int:pk>/update/', views.WizardUpdate.as_view(), name='wizard_update'),
    path('main/<int:pk>/delete', views.WizardDelete.as_view(), name='wizard_delete'),
    path('lookup/', views.HouseView.as_view(), name='house_list'),
    path('lookup/create/', views.HouseCreate.as_view(), name='house_create'),
    path('lookup/<int:pk>/update', views.HouseUpdate.as_view(), name='house_update'),
    path('lookup/create/<int:pk>/delete', views.HouseDelete.as_view(), name='house_delete'),
]
