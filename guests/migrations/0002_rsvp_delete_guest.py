# Generated by Django 5.2.1 on 2025-05-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('attending', models.BooleanField(verbose_name='Присутствует')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Пожелания')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]
