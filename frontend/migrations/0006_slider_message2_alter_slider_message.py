# Generated by Django 4.2.16 on 2024-12-10 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_remove_slider_message2'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='message2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='message',
            field=models.CharField(max_length=15),
        ),
    ]