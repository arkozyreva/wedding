from django.db import models


class RSVP(models.Model):
    full_name = models.CharField('ФИО', max_length=100)

    ATTENDING_CHOICES = [
        ('yes', 'Я приду / Мы придем'),
        ('no', 'К сожалению, не смогу'),
    ]
    attending = models.CharField(
        'Присутствие',
        max_length=3,
        choices=ATTENDING_CHOICES
    )

    ALCOHOL_CHOICES = [
        ('вино красное', 'Вино красное'),
        ('вино белое', 'Вино белое'),
        ('шампанское', 'Шампанское'),
        ('виски', 'Виски'),
        ('водка', 'Водка'),
        ('самогон', 'Самогон'),
        ('безалкогольное', 'Что-то безалкогольное'),
    ]
    alcohol_choices = models.CharField(
        'Алкогольные предпочтения',
        max_length=200,
        blank=True
    )

    # created_at = models.DateTimeField('Дата ответа', auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.get_attending_display()})"