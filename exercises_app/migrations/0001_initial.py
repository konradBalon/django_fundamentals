# Generated by Django 2.2.6 on 2021-09-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('released_year', models.IntegerField()),
                ('score', models.IntegerField(choices=[(0, ''), (1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'), (6, '******')])),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=64, null=True)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'writing in progress'), (2, 'waiting for approval'), (3, 'published')])),
                ('date_publish', models.DateTimeField(null=True)),
                ('date_unpublish', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('year', models.IntegerField(null=True)),
                ('still_active', models.BooleanField(default=True)),
                ('genre', models.IntegerField(choices=[(-1, 'not defined'), (0, 'rock'), (1, 'metal'), (2, 'pop'), (2, 'pop'), (3, 'hip - hop,'), (4, 'electronic'), (5, 'reggae'), (6, 'other')], default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
    ]
