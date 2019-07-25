from django.shortcuts import render
from guest_app.models import Guest

# Create your views here.
def get_guests(request):
    guests = Guest.objects.all()
    return render(request, 'guest_list.html', {
        'guests': guests 
    })

