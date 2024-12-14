from django.conf import settings
from django.db import models


class Category(models.Model):
    """модель для категорий товаров"""
    name = models.CharField(max_length = 200, db_index = True)
    # поле под ссылку на категорию
    slug = models.SlugField(max_length = 200, unique = True)
    image = models.ImageField(upload_to='images/category', default = 'image/default.jpg' , blank = True)
    description = models.TextField(blank = True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name

class Product(models.Model):
    """модель для товаров"""
    category = models.ForeignKey(Category, related_name = 'product', on_delete = models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # имя и ссылка
    name = models.CharField(max_length = 50, db_index = True)
    slug = models.SlugField(max_length = 100, db_index = True, unique = True)
    # фото
    image = models.ImageField(upload_to=f'images/products/%Y/%m/%d', default = 'images/default/product.jpg', blank = True)
    # размер
    # size = 
    # описание
    description = models.TextField(blank = True,)
    # цена
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    # дата добавления продукта
    created = models.DateTimeField(auto_now_add = True)

    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
        # index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name

    def tags(self):
        """получение тегов из описания товара"""
        tags = []
        for word in self.description.split(' '):
            if word[0] == '#':
                tags.append(word)
        return tags