# Generated by Django 4.1.3 on 2022-12-14 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Virtual_Gallery', '0009_obraz_slug_alter_obraz_wlasciciel_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obraz',
            name='slug',
        ),
    ]