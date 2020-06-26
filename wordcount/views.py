from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html', {"name": "Aswathi"})

def test(request):
    return HttpResponse("<h3>Testing in progress</h3>")

def count(request):
    fulText = request.GET['fullText']
    wordsCount =  len(fulText.split())
    worddictionary = {}
    for word in fulText.split():
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    return render(request, 'count.html', {"fullText": fulText, "Count": wordsCount , "worddictionary": worddictionary.items()})
    
    