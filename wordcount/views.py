from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html',)

def count(request):
    fulltext = request.GET['fulltext']
    wordlist=fulltext.split()
    noofword=len(wordlist)
    count=0
    for word in wordlist:
        for char in word:
            
            count+=1
    avgchars=count/noofword
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'avg':avgchars,})

def about(request):
    return render(request,'about.html',)
