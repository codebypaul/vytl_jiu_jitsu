# Generated by Django 4.2.6 on 2023-11-08 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0005_class_attend_class_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='attend',
            name='class_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
