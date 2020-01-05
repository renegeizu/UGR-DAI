from django.shortcuts import render

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {}
    return render(request,'test.html', context)
