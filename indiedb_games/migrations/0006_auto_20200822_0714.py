# Generated by Django 3.1 on 2020-08-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indiedb_games', '0005_game_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='url',
            field=models.CharField(default='#', max_length=255),
        ),
    ]
