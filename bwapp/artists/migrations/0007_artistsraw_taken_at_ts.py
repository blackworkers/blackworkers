# Generated by Django 2.1.1 on 2018-09-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0006_auto_20180913_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistsraw',
            name='taken_at_ts',
            field=models.DateTimeField(null=True),
        ),
    ]
