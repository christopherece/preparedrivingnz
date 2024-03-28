# Generated by Django 4.2.1 on 2023-05-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_option_explanation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='explanation',
        ),
        migrations.AddField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
