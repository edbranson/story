# Generated by Django 3.2.12 on 2022-03-15 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_tags_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='media',
        ),
    ]