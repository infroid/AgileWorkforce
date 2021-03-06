# Generated by Django 2.2.1 on 2019-05-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('country', 'state', 'name')},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('role', 'profile')},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('user',)},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ('country', 'name')},
        ),
    ]
