from django.shortcuts import render, redirect
from .forms import GuestForm
from django.contrib import messages

from .models import RSVP


def wedding_invite(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get('full_name')
            attending = request.POST.get('attending')
            alcohol = request.POST.getlist('alcohol')  # Получаем список выбранных значений

            # Сохраняем в модель
            rsvp = RSVP(
                full_name=full_name,
                attending=attending,
                alcohol_choices=','.join(alcohol)  # Сохраняем как строку через запятую
            )
            rsvp.save()
            return redirect('/guests/thank_you/')  # или другой URL
    else:
        form = GuestForm()
    return render(request, 'guests/invite.html', {'form': form})

def thank_you(request):
    return render(request, 'guests/thank_you.html')