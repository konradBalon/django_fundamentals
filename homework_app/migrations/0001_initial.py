# Generated by Django 3.0.3 on 2021-09-19 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PersonMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=128)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework_app.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework_app.Person')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directors', to='homework_app.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='homework_app.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='screenplay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenplays', to='homework_app.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='starring',
            field=models.ManyToManyField(through='homework_app.PersonMovie', to='homework_app.Person'),
        ),
    ]
