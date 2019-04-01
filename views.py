from django.http import HttpResponse
from django.shortcuts import render

def index(request):
        
        return render(request, 'index.html')

   # return HttpResponse('<h1>Hi This is fawaz</h1>')


def about(request):
    return HttpResponse('<p>Hi This is about page</p>')

def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)

def Home(request):
        return HttpResponse("Home")

def analyze(request):
        #Get the text
        djtext = request.POST.get('text','default')
        #check checkbox values
        removepunc = request.POST.get('removepunc','off')
        fullcaps = request.POST.get('fullcaps','off')
        newlineremover = request.POST.get('newlineremover','off')
        spaceremover = request.POST.get('spaceremover','off')
        charcount = request.POST.get('charcount','off')
        #check with check box on
        if removepunc == "on":
                punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
                analyzed = ""
                for char in djtext:
                        if char not in punctuations:
                                analyzed = analyzed + char
                params = {'purpose':'Removed Punctuations' ,'analyzed_text': analyzed} 
        #analyze the text
                return render(request,'analyze.html',params)
        elif(fullcaps == 'on'):
                analyzed=""
                for char in djtext:
                        analyzed = analyzed + char.upper()
                params = {'purpose':'Change to Uppercase' ,'analyzed_text': analyzed} 
                return render(request,'analyze.html',params)
        
        elif(newlineremover == 'on'):
                analyzed=""
                for char in djtext:
                        if char !='\n'and char!='\r':
                                analyzed = analyzed + char
                params = {'purpose':'Remove New Lines' ,'analyzed_text': analyzed} 
                return render(request,'analyze.html',params)

        elif(spaceremover == 'on'):
                analyzed=""
                for index, char in enumerate (djtext):
                        if djtext[index] ==" " and djtext[index+1] == ' ':
                                pass
                        else:
                                analyzed = analyzed + char
                params = {'purpose':'Remove New Lines' ,'analyzed_text': analyzed} 
                return render(request,'analyze.html',params)

        elif(charcount == 'on'):
                analyzed=""
                for char in djtext:
                        analyzed=len(djtext)

                
                params = {'purpose':'Charcter Count' ,'analyzed_text': analyzed} 
                return render(request,'analyze.html',params)

                                

        else:
                return HttpResponse('Error')

# def capitalizefirst(request):
#         return HttpResponse("Capitalize First")

# def newlineremove(request):
#         return HttpResponse("NewLineRemover")

# def spaceremove(request):
#         return HttpResponse("SpaceRemove <a href='/'>Back </a>")

# def charcount(request):
#         return HttpResponse("CharCount")
