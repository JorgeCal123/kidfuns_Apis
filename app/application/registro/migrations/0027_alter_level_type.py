# Generated by Django 3.2.4 on 2022-07-07 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0026_level_lvl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
