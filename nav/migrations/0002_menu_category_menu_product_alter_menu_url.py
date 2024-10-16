# Generated by Django 4.2.16 on 2024-10-15 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0027_attributeoption_code_attributeoptiongroup_code_and_more'),
        ('nav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.category'),
        ),
        migrations.AddField(
            model_name='menu',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.product'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(blank=True, null=True),
        ),
    ]
