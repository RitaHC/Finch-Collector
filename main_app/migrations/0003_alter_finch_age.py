# Generated by Django 4.1.7 on 2023-03-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_img_finch_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finch',
            name='age',
            field=models.IntegerField(),
        ),
    ]
