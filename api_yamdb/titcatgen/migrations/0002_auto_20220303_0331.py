# Generated by Django 3.0 on 2022-03-03 00:31

import django.db.models.deletion
from django.db import migrations, models

import titcatgen.validators


class Migration(migrations.Migration):

    dependencies = [
        ('titcatgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('slug',)},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('slug',)},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='titcatgen.Category'),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='titles', to='titcatgen.Genre'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[titcatgen.validators.max_value_this_year, titcatgen.validators.min_value_first_year]),
        ),
    ]
