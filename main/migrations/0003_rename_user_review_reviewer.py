# Generated by Django 5.0.6 on 2024-07-01 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='reviewer',
        ),
    ]