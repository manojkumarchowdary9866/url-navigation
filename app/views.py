from django.shortcuts import render

# Create your views here.
def p1url(request):
    return render(request,'p1url.html')
def p2(request):
    return render(request,'p2.html')