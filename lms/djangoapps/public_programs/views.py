import requests
from django.shortcuts import render

def public_programs(request, program_uuid=None):

    # Case 1: Program detail page
    if program_uuid:
        api_url = f"https://discovery.unify.university/api/v1/programs/{program_uuid}/"
        response = requests.get(api_url)

        if response.status_code != 200:
            return render(request, "404.html", status=404)

        program = response.json()

        # 👉 Render the NEW details template
        return render(
            request,
            "public_programs/public-programs-detail.html",
            {"program": program}
        )

    # Case 2: Program list page
    api_url = "https://discovery.unify.university/api/v1/programs/"
    response = requests.get(api_url).json()

    programs = response.get("results", [])

    return render(
        request,
        "public_programs/public-programs.html",
        {"programs": programs}
    )
