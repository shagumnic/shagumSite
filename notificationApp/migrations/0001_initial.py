# Generated by Django 3.0.6 on 2020-05-21 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGamesList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steamId', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('concurrentPlayers', models.IntegerField(null=True)),
                ('release_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('genre', models.CharField(max_length=200)),
                ('rating', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('preview_image', models.CharField(max_length=200)),
                ('videoGamesList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificationApp.VideoGamesList')),
            ],
        ),
        migrations.CreateModel(
            name='RedditNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redditUrl', models.CharField(max_length=200)),
                ('redditName', models.CharField(max_length=200)),
                ('redditDescription', models.CharField(max_length=200)),
                ('videoGame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificationApp.VideoGame')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial', models.CharField(max_length=200, null=True)),
                ('final', models.CharField(max_length=200, null=True)),
                ('discount_percent', models.IntegerField(null=True)),
                ('videoGame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificationApp.VideoGame')),
            ],
        ),
    ]
