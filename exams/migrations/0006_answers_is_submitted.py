# Generated by Django 3.1.5 on 2021-01-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_remove_answers_is_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
