from django.db import models

class discribe(models.Model):
    title = models.CharField('Name', max_length=50, default='')
    anons = models.CharField('Anons', max_length=250, default='')
    full_text = models.TextField('Fulltext')
    image = models.ImageField('Image', upload_to='images/', default='')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/pages/{self.id}'

    class Meta:
        verbose_name = 'discribe'
        verbose_name_plural = 'discribes'

