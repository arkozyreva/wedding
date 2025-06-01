# from django import forms
# from .models import RSVP
#
# ATTENDING_CHOICES = [
#     ('yes', 'Я приду / Мы придем'),
#     ('no', 'К сожалению, не смогу'),
# ]
#
# ALCOHOL_CHOICES = [
#     ('вино красное', 'Вино красное'),
#     ('вино белое', 'Вино белое'),
#     ('шампанское', 'Шампанское'),
#     ('виски', 'Виски'),
#     ('водка', 'Водка'),
#     ('самогон', 'Самогон'),
#     ('безалкогольное', 'Что-то безалкогольное'),
# ]
#
# class GuestForm(forms.ModelForm):
#     class Meta:
#         model = RSVP
#         fields = ['full_name', 'attending', 'alcohol_choices']
#         widgets = {
#             'full_name': forms.TextInput(attrs={'placeholder': 'Ваше полное имя'}),
#             'attending': forms.RadioSelect(choices=ATTENDING_CHOICES),
#             'alcohol_choices': forms.CheckboxSelectMultiple(choices=ALCOHOL_CHOICES),
#         }
#         labels = {
#             'full_name': 'Пожалуйста, укажите ФИО для подтверждения',
#             'attending': 'Придёте ли вы на нашу свадьбу?',
#             'alcohol_choices': 'Какой алкоголь вы будете пить? (можно выбрать несколько вариантов)',
#         }

from django import forms
from .models import RSVP


class GuestForm(forms.ModelForm):
    alcohol_choices = forms.MultipleChoiceField(
        choices=RSVP.ALCOHOL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = RSVP
        fields = ['full_name', 'attending', 'alcohol_choices']
        widgets = {
            'attending': forms.RadioSelect,
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.alcohol_choices = ','.join(self.cleaned_data['alcohol_choices'])
        if commit:
            instance.save()
        return instance