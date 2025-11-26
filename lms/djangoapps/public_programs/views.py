import requests
from django.shortcuts import render

def public_programs(request):
    api_url = "https://discovery.unify.university/api/v1/programs/"
    response = requests.get(api_url).json()

    programs = response.get("results", [])
    return render(request, "public_programs/public_programs.html", {"programs": programs})