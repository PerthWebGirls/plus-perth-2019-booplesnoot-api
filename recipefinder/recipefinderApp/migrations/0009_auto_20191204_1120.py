# Generated by Django 2.2.7 on 2019-12-04 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipefinderApp', '0008_auto_20191204_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cooktime',
            options={'ordering': ('cook_times',)},
        ),
        migrations.AlterModelOptions(
            name='diet',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dietrequirement',
            options={'ordering': ('user',)},
        ),
        migrations.AlterModelOptions(
            name='preferences',
            options={'ordering': ('user',)},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('user',)},
        ),
    ]
