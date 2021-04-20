from django.shortcuts import render

# Create your views here.
def meet(request, room_id):

    return render(request, "meets/meet.html")