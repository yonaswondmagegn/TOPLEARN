# Generated by Django 4.1.7 on 2023-03-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='grade_level',
            field=models.IntegerField(),
        ),
    ]