# Generated by Django 2.2.1 on 2019-05-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sprint', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={'ordering': ('sprint', 'name')},
        ),
        migrations.AlterModelOptions(
            name='sprint',
            options={'ordering': ('user', 'start_date')},
        ),
    ]