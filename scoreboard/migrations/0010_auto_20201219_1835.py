# Generated by Django 3.1.3 on 2020-12-19 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0009_auto_20201218_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='playerscore',
            field=models.CharField(choices=[(5, 'A'), (4, 'B'), (3, 'C'), (2, 'D'), (1, 'E'), (0, 'F')], max_length=1),
        ),
    ]
