# Generated by Django 4.0.5 on 2022-06-28 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0014_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]