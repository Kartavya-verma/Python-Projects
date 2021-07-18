from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course1(request):
    # return HttpResponse("PCM")
    return render(request,'course/course1.html')

def course2(request):
    # return HttpResponse("PCM")
    return render(request,'course/course2.html')