# Generated by Django 3.1 on 2020-08-21 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indiedb_games', '0002_auto_20200820_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='indiedb_games.game')),
            ],
        ),
    ]