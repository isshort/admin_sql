# Generated by Django 3.1 on 2020-09-01 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nx', '0018_auto_20200901_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finance',
            options={'ordering': ['-type']},
        ),
    ]