# Generated by Django 3.1 on 2021-04-29 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Experience', '0002_auto_20210429_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencemodel',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date(1984, 11, 24)),
        ),
        migrations.AlterField(
            model_name='experiencemodel',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(1984, 11, 24)),
        ),
    ]