# Generated by Django 3.1.3 on 2020-12-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0005_auto_20201218_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='player1score',
            field=models.CharField(choices=[('5', 'A'), ('4', 'B'), ('3', 'C'), ('2', 'D'), ('1', 'E'), ('0', 'F')], max_length=1),
        ),
        migrations.AlterField(
            model_name='score',
            name='player2score',
            field=models.CharField(choices=[('5', 'A'), ('4', 'B'), ('3', 'C'), ('2', 'D'), ('1', 'E'), ('0', 'F')], max_length=1),
        ),
    ]
