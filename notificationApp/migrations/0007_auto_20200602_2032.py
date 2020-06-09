# Generated by Django 3.0.6 on 2020-06-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificationApp', '0006_auto_20200602_0050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videogame',
            old_name='genre',
            new_name='genres',
        ),
        migrations.AddField(
            model_name='videogame',
            name='tags',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='released_date',
            field=models.DateField(null=True),
        ),
    ]
