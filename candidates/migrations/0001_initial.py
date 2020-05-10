# Generated by Django 3.0.2 on 2020-01-28 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalCoalition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('RENOVACIÓN NACIONAL', 'Renovación Nacional'), ('PARTIDO COMUNISTA', 'Partido Comunista')], max_length=100)),
                ('nickname', models.CharField(choices=[('RN', 'RN'), ('PC', 'PC')], max_length=50)),
                ('political_side', models.CharField(choices=[('IZQUIERDA', 'Izquierda'), ('CENTRO-IZQUIERDA', 'Centro izquierda'), ('CENTRO', 'Centro'), ('CENTRO-DERECHA', 'Centro derecha'), ('DERECHA', 'Derecha')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('age', models.IntegerField(null=True)),
                ('birth_date', models.DateField(null=True)),
                ('state', models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], max_length=30)),
                ('political_coalition', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.PoliticalCoalition')),
            ],
        ),
    ]
