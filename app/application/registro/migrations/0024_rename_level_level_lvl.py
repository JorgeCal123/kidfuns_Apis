# Generated by Django 3.2.4 on 2022-07-07 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0023_auto_20220706_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='level',
            new_name='lvl',
        ),
    ]
