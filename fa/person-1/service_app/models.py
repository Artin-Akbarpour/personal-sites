from django.db import models

# Create your models here.
class service(models.Model):
    icon = models.ImageField('ایکون', upload_to='service/icons')
    name = models.CharField('اسم', max_length=100)
    short = models.TextField('کوتاه')
    img = models.ImageField('عکس', upload_to='service/img')
    body = models.TextField('توضیحات')

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'

    def __str__(self):
        return self.name