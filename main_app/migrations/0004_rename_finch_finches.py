# Generated by Django 4.1.7 on 2023-03-02 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_finch_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Finch',
            new_name='Finches',
        ),
    ]