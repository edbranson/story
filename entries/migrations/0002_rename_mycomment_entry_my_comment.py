# Generated by Django 3.2.12 on 2022-04-28 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='mycomment',
            new_name='my_comment',
        ),
    ]
