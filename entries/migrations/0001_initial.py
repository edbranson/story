# Generated by Django 3.2.12 on 2022-03-15 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0001_initial'),
        ('profiles', '0002_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=25)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('mycomment', models.CharField(blank=True, max_length=100)),
                ('review', models.TextField(blank=True, max_length=2000)),
                ('recommended_by', models.CharField(blank=True, max_length=30)),
                ('status', models.CharField(choices=[('FINISHED', 'Finished'), ('STARTED', 'Started'), ('WISHLIST', 'Wish List')], max_length=10)),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_finished', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('media', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='media.media')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='profiles.profile')),
            ],
        ),
    ]