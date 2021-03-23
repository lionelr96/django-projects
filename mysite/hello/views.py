from django.shortcuts import render
from django.http import HttpResponse
# from visits.models import Visits

# Create your views here.
def cookie(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    res = HttpResponse(f"view count={num_visits}")
    res.set_cookie('dj4e_cookie', '2fe10492', max_age=1000)
    return res
    # return HttpResponse('Hello!')
