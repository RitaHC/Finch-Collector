# Generated by Django 4.1.7 on 2023-03-02 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finch',
            old_name='img',
            new_name='age',
        ),
    ]