from django.contrib import admin
from .models import RSVP


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'attending', 'get_alcohol_list')

    def get_alcohol_list(self, obj):
        return obj.alcohol_choices.replace(',', ', ') if obj.alcohol_choices else '-'

    get_alcohol_list.short_description = 'Алкоголь'