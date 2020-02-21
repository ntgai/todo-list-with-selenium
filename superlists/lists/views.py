from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        return render(request, 'lists/home.html', {'new_item_text':new_item_text})
    return render(request, 'lists/home.html', {})
