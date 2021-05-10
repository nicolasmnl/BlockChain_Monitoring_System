# Generated by Django 3.2 on 2021-05-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id_industry', models.AutoField(primary_key=True, serialize=False)),
                ('volume_resfriamento', models.FloatField()),
                ('dia_hora_resfriamento', models.DateTimeField()),
                ('temperatura_resfriamento', models.FloatField()),
                ('ph_resfriamento', models.FloatField()),
                ('volume_envase', models.FloatField()),
                ('dia_hora_envase', models.DateTimeField()),
                ('lote', models.CharField(max_length=11)),
            ],
        ),
    ]
