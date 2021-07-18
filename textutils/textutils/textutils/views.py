#I have created this file....KV

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')

    removepunct = request.POST.get('removepunct', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline', 'off')
    extraspacerem = request.POST.get('extraspacerem', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunct == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
            params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitilize Text', 'analyzed_text': analyzed}
        djtext = analyzed

    if newline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitilize Text', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspacerem == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = ""
        c=0
        for char in djtext:
            if char != " ":
                c+=1
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': 'Total char is: {}'.format(c) }

    if (removepunct != 'on' and fullcaps != 'on' and newline != 'on' and extraspacerem != 'on' and charcount != 'on'):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)


