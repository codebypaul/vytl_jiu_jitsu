# Generated by Django 4.2.6 on 2023-11-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0007_classnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.CharField()),
                ('cost', models.FloatField()),
                ('date_paid', models.DateField()),
                ('paid_to', models.CharField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='membership',
            name='membership_paid',
            field=models.IntegerField(blank=True, choices=[(130, 130), (100, 100)], null=True),
        ),
    ]