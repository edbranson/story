# Generated by Django 3.2.12 on 2022-05-04 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_alter_media_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagged',
            name='media',
        ),
        migrations.AddField(
            model_name='tagged',
            name='media',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='media.media'),
            preserve_default=False,
        ),
    ]
