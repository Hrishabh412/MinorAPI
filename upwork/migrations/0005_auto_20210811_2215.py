# Generated by Django 3.1.7 on 2021-08-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upwork', '0004_auto_20210811_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(max_length=50),
        ),
    ]
