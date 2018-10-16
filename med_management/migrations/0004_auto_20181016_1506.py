# Generated by Django 2.1 on 2018-10-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_management', '0003_auto_20181012_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='medications',
        ),
        migrations.AddField(
            model_name='medication',
            name='patients',
            field=models.ManyToManyField(to='med_management.Patient'),
        ),
    ]
