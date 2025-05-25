from django.shortcuts import render, redirect
from .forms import GuestForm

def wedding_invite(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = GuestForm()
    return render(request, 'guests/invite.html', {'form': form})