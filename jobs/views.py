from django.shortcuts import render
from .models import Jobs

def encontrar_jobs(request):
    if request.method == "GET":
        jobs = Jobs.objects.filter(reservado=False)
        return render(request, 'encontrar_jobs.html', {'jobs': jobs})
