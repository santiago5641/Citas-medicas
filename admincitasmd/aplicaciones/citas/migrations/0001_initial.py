# Generated by Django 3.2.9 on 2021-11-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('cit_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cit_fecha', models.DateField()),
                ('cit_hora', models.TimeField()),
                ('med_id', models.IntegerField()),
                ('pac_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('esp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('esp_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('med_nombre', models.CharField(max_length=50)),
                ('med_apellido', models.CharField(max_length=50)),
                ('med_id', models.IntegerField(primary_key=True, serialize=False)),
                ('esp_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('pac_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pac_nombre', models.CharField(max_length=50)),
                ('pac_apellido', models.CharField(max_length=50)),
                ('pac_ced_ruc', models.CharField(max_length=13)),
                ('pac_cell_telf', models.JSONField()),
            ],
        ),
    ]
