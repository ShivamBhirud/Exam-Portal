# Generated by Django 3.1.5 on 2021-01-08 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_answers_is_submitted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='is_submitted',
        ),
    ]
