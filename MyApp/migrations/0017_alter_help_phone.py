# Generated by Django 3.2.9 on 2022-01-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0016_alter_help_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help',
            name='phone',
            field=models.CharField(default=1234567890, max_length=11),
            preserve_default=False,
        ),
    ]
