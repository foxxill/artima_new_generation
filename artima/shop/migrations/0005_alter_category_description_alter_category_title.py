# Generated by Django 5.1.4 on 2024-12-16 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
