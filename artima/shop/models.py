from django.db import models


class Category(models.Model):
    """модель для категорий продуктов"""
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
    
    def tags(self):
        tags = []
        for word in self.description.split(' '):
            if word[0] == '#':
                tags.append(word)
        return tags
