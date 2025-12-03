import requests
from django.shortcuts import render

def public_programs(request, program_uuid=None):

    
    if program_uuid:
        api_url = f"https://discovery.unify.university/api/v1/programs/{program_uuid}/"
        response = requests.get(api_url)

        if response.status_code != 200:
            return render(request, "404.html", status=404)

        program = response.json()
        return render(request, "public_programs/public_programs.html", {"program": program, "programs": None})


    api_url = "https://discovery.unify.university/api/v1/programs/"
    response = requests.get(api_url).json()

    programs = response.get("results", [])
    return render(request, "public_programs/public_programs.html", {"programs": programs})
