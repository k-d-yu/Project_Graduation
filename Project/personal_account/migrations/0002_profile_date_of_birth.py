# Generated by Django 4.1.7 on 2023-05-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]