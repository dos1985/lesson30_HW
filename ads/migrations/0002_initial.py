# Generated by Django 4.2 on 2023-05-30 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="admodel",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ads",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AddField(
            model_name="admodel",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ads.categorymodel"
            ),
        ),
    ]
