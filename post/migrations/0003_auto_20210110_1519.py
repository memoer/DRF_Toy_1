# Generated by Django 3.1.5 on 2021-01-10 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210110_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
    ]