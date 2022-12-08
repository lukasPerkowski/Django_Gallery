# Generated by Django 4.1.3 on 2022-12-05 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Virtual_Gallery', '0005_alter_obraz_wlasciciel_zamowienie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obraz',
            name='wlasciciel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='zamawiajcy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]