# Generated by Django 3.2.12 on 2022-05-13 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0014_alter_media_ave_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0007_auto_20220511_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='media',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='media.media'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]