# Generated by Django 3.1.5 on 2021-01-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
