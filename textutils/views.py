# I have created this file

#
# CODE OF VIDEO 6
# def index(request):
#     return HttpResponse('''<h1> hello </h1><a href="https://www.facebook.com/"> Facebook.com </a>''')
# def about(request):
#     return HttpResponse("ABOUT hello")

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', )
    # return HttpResponse("Home")

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # check box value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newLineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # print(removepunc)
    # print(djtext)
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                   analyzed =analyzed + char
        params = {'purpose': 'Removed puncutations', 'analyzed_text': analyzed}
        djtext = analyzed
    #     return render(request, 'analyze.html',params)
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'change to upppercase', 'analyzed_text': analyzed}
        djtext= analyzed
        # return render(request, 'analyze.html', params)
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        params = {'purpose': 'Remove Newlines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover =="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)

        params = {'purpose': 'Remove Newlines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if( removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse("Please select any operation")


    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("spaceremove")
# def charcount(request):
#     return HttpResponse("charcount")
