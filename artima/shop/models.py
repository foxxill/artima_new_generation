from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """модель для категорий товаров"""
    name = models.CharField(max_length = 200, db_index = True)
    # поле под ссылку на категорию
    slug = models.SlugField(max_length = 200, unique = True)
    # поля для открытой категории
    title = models.CharField(max_length = 200, default = '', blank=True)
    description = models.CharField(max_length = 500, default = '', blank=True)
    
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
    name = models.CharField(max_length = 150, db_index = True)
    slug = models.SlugField(max_length = 250, db_index = True, unique = True)
    # фото
    image = models.ImageField(upload_to=f'images/products/%Y/%m/%d', default = 'images/default/product.jpg', blank = True)
    # размер
    hight = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    # цвет
    color = models.CharField(max_length = 500, blank=True, null=True)
    # тематика
    theme = models.CharField(max_length = 500, blank=True, null=True)
    # описание
    description = models.TextField(blank = True,)
    # цена
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    # наличие
    avialable = models.BooleanField(default=True)
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
                if word[1::] != '': tags.append(word[1::])
        return tags


class AdvancedProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='images/profile', default='images/default/profile.jpg')
    # фио
    name = models.CharField(max_length = 30, default='')
    surname = models.CharField(max_length = 30, default='')
    secondname = models.CharField(max_length = 30, default='')
    # телефон
    number = models.IntegerField(blank=True, null=True)
    # адресс
    country = models.CharField(max_length = 30, default='')
    city = models.CharField(max_length = 30, default='')
    address = models.CharField(max_length = 200, default='')
    # о себе
    about = models.TextField(blank = True)

    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'
    
    def __str__(self):
        return f'{self.user.username} Profile'
    

class OrdinaryProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # фио
    name = models.CharField(max_length = 30, default='')
    surname = models.CharField(max_length = 30, default='')
    secondname = models.CharField(max_length = 30, default='')
    # телефон
    number = models.IntegerField(blank=True, null=True)
    # адресс
    country = models.CharField(max_length = 30, default='')
    city = models.CharField(max_length = 30, default='')
    address = models.CharField(max_length = 200, db_index = True, default='')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
    
    def __str__(self):
        return f'{self.user.username} Profile'
    

class Bag (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Commentary(models.Model):
    profile = models.ForeignKey(AdvancedProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(OrdinaryProfile, on_delete=models.CASCADE)

    class Meta:
        ordering = ('user',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



