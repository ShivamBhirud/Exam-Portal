# Generated by Django 3.1.5 on 2021-01-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_auto_20210108_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]