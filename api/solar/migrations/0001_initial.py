# Generated by Django 5.1.2 on 2024-11-03 20:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_placas', models.IntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxValueValidator(180)])),
                ('valor_placa', models.FloatField(validators=[django.core.validators.MinLengthValidator(1)])),
                ('valor_energia', models.FloatField(validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
    ]
