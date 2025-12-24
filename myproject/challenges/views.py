from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
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

def monthly_challenges_by_num(request,month):
  months = list(challenges.keys())
  
  if month > len(months):
    return HttpResponseNotFound("Invalid number")
  
  redirect_month = months[month - 1]
  return HttpResponseRedirect('/challenges/'+ redirect_month)


def monthly_challenges(request,month):
  try:
    challenges_text = challenges[month]
    return HttpResponse(challenges_text)
  except:
    return HttpResponseNotFound("This is not a valid months")