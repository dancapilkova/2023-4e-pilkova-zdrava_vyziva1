# Generated by Django 5.0.3 on 2024-04-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("socials", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="dob",
            field=models.DateField(default="2000-01-01", max_length=8),
        ),
    ]
