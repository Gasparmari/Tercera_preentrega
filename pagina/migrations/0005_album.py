# Generated by Django 4.1.7 on 2023-03-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_alter_cancion_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('autor', models.CharField(max_length=20)),
                ('anio_de_lanzamiento', models.CharField(max_length=20)),
            ],
        ),
    ]