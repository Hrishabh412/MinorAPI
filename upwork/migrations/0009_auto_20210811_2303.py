# Generated by Django 3.1.7 on 2021-08-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upwork', '0008_auto_20210811_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobileno',
            field=models.IntegerField(max_length=10),
        ),
    ]
