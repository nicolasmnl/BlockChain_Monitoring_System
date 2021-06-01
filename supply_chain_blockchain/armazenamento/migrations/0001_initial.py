# Generated by Django 3.2 on 2021-06-01 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armazenamento',
            fields=[
                ('block_index', models.IntegerField()),
                ('block_timestamp', models.DateTimeField(auto_now_add=True)),
                ('block_nonce', models.IntegerField()),
                ('data', models.DateTimeField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('volume_tanque_hora_final', models.IntegerField()),
                ('block_hash', models.TextField(default='a45e883014fb62000b041977b626f1eb718e84b973f344b12a8a878be6c41eeb', primary_key=True, serialize=False)),
            ],
        ),
    ]