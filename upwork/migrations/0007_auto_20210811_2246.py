# Generated by Django 3.1.7 on 2021-08-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upwork', '0006_auto_20210811_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
