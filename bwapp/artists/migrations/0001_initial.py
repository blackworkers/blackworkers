# Generated by Django 2.1.1 on 2018-09-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistsRaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_handle', models.CharField(help_text='Enter an artists instagram handle', max_length=200)),
                ('caption', models.CharField(help_text='Enter the artists post caption', max_length=200)),
                ('shortcode', models.CharField(help_text='Enter the posts shortcode', max_length=200)),
                ('city', models.CharField(help_text='Enter the artists city', max_length=200)),
                ('state', models.CharField(help_text='Enter the artists state', max_length=200)),
                ('likes', models.IntegerField()),
                ('display_url', models.URLField()),
            ],
        ),
    ]