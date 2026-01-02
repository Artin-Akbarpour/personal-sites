from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField('نام و نام خانوادگی', max_length=100)
    email = models.EmailField('ایمیل')
    phone = models.CharField('شماره تماس', max_length=100)
    subject = models.CharField('موضوع', max_length=100)
    message = models.TextField('پیام')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ' کاربر'
