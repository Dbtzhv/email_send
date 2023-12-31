# Generated by Django 4.2.2 on 2023-06-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("to", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=64)),
                ("message", models.TextField()),
            ],
        ),
    ]
