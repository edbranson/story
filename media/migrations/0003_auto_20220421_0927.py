# Generated by Django 3.2.12 on 2022-04-21 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_tagged'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagged',
            name='media',
        ),
        migrations.AddField(
            model_name='tagged',
            name='media',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, to='media.media'),
            preserve_default=False,
        ),
    ]
