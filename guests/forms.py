from django import forms
from .models import RSVP

class GuestForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['full_name', 'attending', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Ваше полное имя'}),
            'attending': forms.RadioSelect(choices=[(True, 'Я приду'), (False, 'К сожалению, не смогу')]),
            'message': forms.Textarea(attrs={'placeholder': 'Пожелания (по желанию)', 'rows': 3}),
        }