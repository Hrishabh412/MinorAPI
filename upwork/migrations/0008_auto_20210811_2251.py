# Generated by Django 3.1.7 on 2021-08-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upwork', '0007_auto_20210811_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(max_length=10),
        ),
    ]
