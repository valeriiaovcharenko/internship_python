from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render


monthly_challenges = {
    "january": "Practice mindfulness for at least 10 minutes each day",
    "february": "Write down three things you are grateful for each day",
    "march": "Commit to at least 30 minutes of physical activity every day",
    "april": "Eliminate added sugars from your diet for the entire month",
    "may": "Read at least one book per week (four books total)",
    "june": "Declutter a different area of your home each day",
    "july": "Try a new creative activity each week",
    "august": "Limit your screen time each day to focus on offline activities",
    "september": "Perform one random act of kindness every day",
    "october": "Track all your expenses for the month and create a budget based on your findings",
    "november": "Try to eat plant-based meals for at least six days a week",
    "december": "Choose a new skill to learn"
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!<h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
