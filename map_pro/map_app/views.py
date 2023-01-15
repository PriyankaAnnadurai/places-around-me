from django.shortcuts import render


def map(request):
    return render(request,"map_app/map.html")
def central(request):
    return render(request,"map_app/central.html")   
def temple(request):
    return render(request,"map_app/temple.html")
def stadium(request):
    return render(request,"map_app/stadium.html")
def museum(request):
    return render(request,"map_app/museum.html")
def highcourt(request):
    return render(request,"map_app/highcourt.html")