# Generated by Django 3.2 on 2021-04-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0004_alter_block_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='hash',
            field=models.TextField(default='b642aaecf583ab65d2f4edc70e1ce607b97990c938c990291ae9ec9db04c610f', primary_key=True, serialize=False),
        ),
    ]
