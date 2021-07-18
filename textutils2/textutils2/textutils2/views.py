from django.http import HttpResponse


def index(request):
    return HttpResponse("KV")


def about(request):
    return HttpResponse("About KV")


def txtfile(request):
    with open("C:/Users/Kartavya Verma/PycharmProjects/textutils2/textutils2/textutils2/1.txt", "r") as f:
        a = f.read()
        return HttpResponse(a)


def nav(request):
    s = '''<h2>Navigation Bar<br></h2>
                <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
                <a href="https://www.facebook.com/">Facebook</a><br>

                <a href="https://www.flipkart.com/">Flipkart</a><br>

                <a href="https://www.hindustantimes.com
    ">News</a><br>
                <a href="https://www.google.com/">Google</a>'''

    return HttpResponse(s)


def removepunc(request):
    return HttpResponse("remove punc")


def capfirst(request):
    return HttpResponse("capitalize first")


def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")


def charcount(request):
    return HttpResponse("charcount ")
