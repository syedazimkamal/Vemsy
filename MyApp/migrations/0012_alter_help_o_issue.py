# Generated by Django 3.2.9 on 2021-12-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0011_alter_help_o_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help',
            name='o_issue',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
