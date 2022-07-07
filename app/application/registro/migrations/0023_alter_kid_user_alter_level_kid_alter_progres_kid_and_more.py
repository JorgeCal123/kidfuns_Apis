# Generated by Django 4.0.5 on 2022-07-07 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0022_progres_kid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='kid', to='registro.user'),
        ),
        migrations.AlterField(
            model_name='level',
            name='kid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level', to='registro.kid'),
        ),
        migrations.AlterField(
            model_name='progres',
            name='kid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progres', to='registro.kid'),
        ),
        migrations.AlterField(
            model_name='progres',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progres', to='registro.level'),
        ),
    ]
