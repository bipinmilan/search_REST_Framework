# Generated by Django 2.1.7 on 2019-12-11 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Chained', '0003_auto_20191211_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chained.Country'),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities', to='Chained.City'),
        ),
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countries', to='Chained.Country'),
        ),
    ]