# Generated by Django 3.2.12 on 2022-05-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_tag_user'),
        ('entries', '0003_alter_entry_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='profiles.Tag'),
        ),
    ]