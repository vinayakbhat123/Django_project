from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
# Create your views here.

challenges = {
  "januvary":"Eat no JunckFood",
  "february":"Walk daily",
  "march":"hit the jim",
  "april":"Do some exercise",
  "may":"Go outside",
  "june":"always happy",
  "july":"Go for trip",
  "august":"hit the jim",
  "september":"go walk",
  "october":"It my birthday months",
  "november":"go cycling",
  "december":"walk daily"
}

def index(request):
  list_months =""
  months = list(challenges.keys())

  for month in months:
    capitalize_month = month.capitalize()
    month_path= reverse("month-challenges",args=[month])
    list_months += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"

  response_data = f"<ul>{list_months}</ul>"
  return HttpResponse(response_data)

def monthly_challenges_by_num(request,month):
  months = list(challenges.keys())
  
  if month > len(months):
    return HttpResponseNotFound("Invalid number")
  
  redirect_month = months[month - 1]
    # reverse(name_url,args)
  redirect_path = reverse("month-challenges",args=[redirect_month])  # /challenges/januvary
  return HttpResponseRedirect(redirect_path)
  # return HttpResponseRedirect('/challenges/'+ redirect_month)


def monthly_challenges(request,month):
  try:
    challenges_text = challenges[month]
    html_text = render_to_string('challenges/challenge.html')
    return HttpResponse(html_text)
  except:
    return HttpResponseNotFound("This is not a valid months")