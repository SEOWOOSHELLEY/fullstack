from django.shortcuts import render

# Create your views here.
def coronamap(request):
    return render(
        request,
        'main_page/button_test.html',
    )