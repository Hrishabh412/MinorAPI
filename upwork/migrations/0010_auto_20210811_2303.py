# Generated by Django 3.1.7 on 2021-08-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upwork', '0009_auto_20210811_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobileno',
            field=models.IntegerField(),
        ),
    ]
