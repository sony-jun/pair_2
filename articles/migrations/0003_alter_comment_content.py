# Generated by Django 3.2.13 on 2022-10-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20221018_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=80),
        ),
    ]
