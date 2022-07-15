from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
def store(request):
    print("--------------Book is calling---------------------")
    result = requests.get(
		'https://www.googleapis.com/books/v1/volumes?',
		 params={
		 'q': "python",
		 "key": settings.GOOGLE_API_KEY
		 })
    books = result.json()
    print(books)


   


    

    
    # return JsonResponse(books)
    return render(request,'store/base.html',{'books':books})



