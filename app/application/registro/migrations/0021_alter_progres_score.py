# Generated by Django 4.0.5 on 2022-07-01 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0020_remove_level_type_progres_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progres',
            name='score',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
