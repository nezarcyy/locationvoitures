# Generated by Django 3.2.13 on 2023-05-06 01:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcvoitures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='date_embauche',
            field=models.DateField(default=datetime.date(2023, 5, 6)),
        ),
    ]