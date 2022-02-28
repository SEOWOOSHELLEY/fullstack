from django.shortcuts import render

# Create your views here.

def coronapage(request):
    return render(
        request,
        'home_page/main_page.html',
    )

def coronamap(request):
    return render(
        request,
        'main_page/map_test.html',
    )