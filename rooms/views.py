from django.shortcuts import render
from meets.models import Meets
# Create your views here.
def index(request):
    rooms = Meets.objects.all()

    context = {
        'rooms': rooms,
    }

    return render(request, 'rooms/index.html', context)