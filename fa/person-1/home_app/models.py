from django.db import models
import django_jalali.db.models as jmodels

# Create your models here.
class person(models.Model):
    name = models.CharField('نام و نام خانوادگی', max_length=100)
    job = models.CharField('شغل', max_length=100)
    img = models.ImageField('عکس سایت', upload_to='img/person/')
    resume = models.FileField('رزومه', upload_to='file/resume/')
    instagram = models.URLField('اینستاگرام')
    youtube = models.URLField('یوتیوب')
    twitter =models.URLField('توییتر')
    facebook = models.URLField('فیسبوک')
    birth_date = jmodels.jDateField('روز تولد')
    email = models.EmailField('ایمیل')
    phone = models.CharField('شماره تلفن', max_length=13)
    address = models.CharField('ادرس', max_length=100)
    Nationality = models.CharField('ملیت', max_length=100)
    experience = models.CharField('سال های تجربه', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شخص'
        verbose_name_plural = 'اشخاص'