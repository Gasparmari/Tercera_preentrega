# Generated by Django 4.1.7 on 2023-03-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_cancion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='autor',
            field=models.CharField(max_length=20),
        ),
    ]
