from django.shortcuts import render
from django.utils.safestring import mark_safe
# Create your views here.


def base(request):
    return render(request, "home.html")