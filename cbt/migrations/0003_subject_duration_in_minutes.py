# Generated by Django 3.0.5 on 2020-05-08 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbt', '0002_auto_20200507_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='duration_in_minutes',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]