# Generated by Django 5.0.7 on 2024-07-28 09:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Alert",
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
                ("cryptocurrency", models.CharField(max_length=50)),
                ("target_price", models.DecimalField(decimal_places=2, max_digits=18)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Created"),
                            ("deleted", "Deleted"),
                            ("tiggered", "Triggered"),
                        ],
                        default="created",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
