# Generated by Django 3.0.5 on 2020-05-07 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qas', to='cbt.Subject'),
        ),
    ]
