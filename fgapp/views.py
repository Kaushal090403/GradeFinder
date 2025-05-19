from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    if request.GET.get("marks"):
        marks=float(request.GET.get("marks"))
        if marks>85:
            grade="A"
        elif marks>75:
            grade="B"
        elif marks>65:
            grade="C"
        else:
            grade="D"
        msg="Ur marks is "+str(marks)+" and grade: "+grade
        return render(request,"home.html",{"msg":msg})
    else:
        return render(request,"home.html")
# Create your views here.
