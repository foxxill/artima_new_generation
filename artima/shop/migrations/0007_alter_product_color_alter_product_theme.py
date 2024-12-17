# Generated by Django 5.1.4 on 2024-12-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_color_theme_rename_autor_product_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(null=True, to='shop.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='theme',
            field=models.ManyToManyField(null=True, to='shop.theme'),
        ),
    ]