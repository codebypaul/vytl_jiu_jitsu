# Generated by Django 4.2.6 on 2023-11-27 00:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("customadmin", "0011_memberincome"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"ordering": ["user__last_name"]},
        ),
    ]