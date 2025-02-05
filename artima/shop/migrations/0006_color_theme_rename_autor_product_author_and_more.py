# Generated by Django 5.1.4 on 2024-12-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_category_description_alter_category_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
                'ordering': ('value',),
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ('value',),
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='avialable',
            new_name='available',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='hight',
            new_name='height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='images/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.RemoveField(
            model_name='product',
            name='theme',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, to='shop.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='theme',
            field=models.ManyToManyField(blank=True, to='shop.theme'),
        ),
    ]
