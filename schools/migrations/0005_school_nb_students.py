# Generated by Django 4.1.7 on 2023-02-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_remove_school_already_graduated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='nb_students',
            field=models.IntegerField(default=0),
        ),
    ]
