# Generated by Django 3.1.3 on 2020-12-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0002_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='round_no',
            field=models.CharField(choices=[('R1', 'R1'), ('R2', 'R2'), ('R3', 'R3'), ('R4', 'R4'), ('R5', 'R5')], max_length=8),
        ),
    ]
