from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField('نام و نام خانوادگی', max_length=100)
    job = models.CharField('شغل', max_length=100)
    img = models.ImageField('عکس', upload_to='images/customer/')
    body = models.TextField('توضیحات')

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
    def __str__(self):
        return self.name
