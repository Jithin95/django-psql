from django.shortcuts import render
from django.http import HttpResponse
from .forms import GuestEntryForm
from .models import GuestEntry, Hit

# Create your views here.
def index(request):
    if request.method == "POST":
        form = GuestEntryForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = GuestEntryForm()

    guestlist =GuestEntry.objects.all()[:10]
    Hit().save()
    hits = Hit.objects.count()

    return render(request, 'home/index.html', {'form' : form, 'guestlist': guestlist, 'hits': hits })
