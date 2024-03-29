# Generated by Django 3.0 on 2022-03-03 00:41

import datetime

import django.db.models.deletion
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('titcatgen', '0002_auto_20220303_0331'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='created',
            new_name='pub_date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=datetime.datetime(2022, 3, 3, 0, 41, 55, 141174, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='reviews.Review'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='titcatgen.Title'),
        ),
    ]
