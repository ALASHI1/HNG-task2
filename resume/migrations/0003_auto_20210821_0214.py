# Generated by Django 3.2.6 on 2021-08-21 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_contactformmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='contact',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]