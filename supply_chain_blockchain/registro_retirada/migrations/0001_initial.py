# Generated by Django 3.2 on 2021-06-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroRetirada',
            fields=[
                ('block_index', models.IntegerField()),
                ('block_timestamp', models.DateTimeField(auto_now_add=True)),
                ('block_nonce', models.IntegerField()),
                ('registro_animal', models.CharField(max_length=5)),
                ('volume', models.FloatField()),
                ('dia_horario', models.DateTimeField()),
                ('block_hash', models.TextField(default='610ad3ae88c37480312cdbea71dc4369fa68c9c68bcd282b81bef9ff3ba725e9', primary_key=True, serialize=False)),
            ],
        ),
    ]
