# Generated by Django 4.2.4 on 2024-03-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_information_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_information',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
