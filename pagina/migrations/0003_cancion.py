# Generated by Django 4.1.7 on 2023-03-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_rename_anio_cantante_anio_de_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('autor', models.IntegerField()),
            ],
        ),
    ]
