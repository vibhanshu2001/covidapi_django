from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    response = requests.get('https://api.covid19api.com/countries').json()
    response2 = requests.get('https://coronavirus-19-api.herokuapp.com/countries').json()
    # response = ''
    # response2=''




    return render(request,'index.html',{'response':response,'response2':response2})