# Generated by Django 4.0.5 on 2022-06-17 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50)),
                ('nombre', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.EmailField(max_length=20)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
    ]
