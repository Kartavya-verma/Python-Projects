from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fee1(request):
    # return HttpResponse("PCM")
    return render(request,'fees/fees1.html')

def fee2(request):
    # return HttpResponse("PCM")
    return render(request,'fees/fees1.html')