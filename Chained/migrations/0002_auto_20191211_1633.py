# Generated by Django 2.1.7 on 2019-12-11 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chained', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='city_name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='name',
            new_name='country_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='person_name',
        ),
    ]