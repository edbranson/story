# Generated by Django 3.2.12 on 2022-05-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_entry_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(choices=[('FINISHED', 'Finished'), ('STARTED', 'Started'), ('WISHLIST', 'Wish List'), ('QUIT', 'Quit')], max_length=10),
        ),
    ]