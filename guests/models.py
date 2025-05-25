from django.db import models


class RSVP(models.Model):
    full_name = models.CharField("ФИО", max_length=200)
    attending = models.BooleanField("Присутствует")
    message = models.TextField("Пожелания", blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


from django.db import models

# Create your models here.
