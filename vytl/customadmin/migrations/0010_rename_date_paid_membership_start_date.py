# Generated by Django 4.2.6 on 2023-11-23 16:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("customadmin", "0009_alter_expense_options_alter_profile_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="membership",
            old_name="date_paid",
            new_name="start_date",
        ),
    ]
