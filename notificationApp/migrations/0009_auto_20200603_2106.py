# Generated by Django 3.0.6 on 2020-06-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificationApp', '0008_discountrate_chosen_discount_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='preview_image',
            field=models.ImageField(max_length=200, null=True, upload_to='game_pics'),
        ),
    ]
