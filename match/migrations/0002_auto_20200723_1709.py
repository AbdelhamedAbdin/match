# Generated by Django 3.0.8 on 2020-07-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playername',
            name='name_box',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
