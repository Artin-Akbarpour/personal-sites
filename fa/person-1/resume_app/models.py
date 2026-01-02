from django.db import models

# Create your models here.
class education(models.Model):
    field = models.CharField('عنوان', max_length=100)
    university = models.CharField('دانشگاه', max_length=100)
    time = models.CharField('بازه زمانی', max_length=100)
    body = models.TextField('توضیحات')

    class Meta:
        verbose_name = 'تحصیل'
        verbose_name_plural = 'تحصیلات'
    def __str__(self):
        return self.field
class experience(models.Model):
    field = models.CharField('عنوان', max_length=100)
    company = models.CharField('شرکت', max_length=100)
    time = models.CharField('بازه زمانی', max_length=100)
    body = models.TextField('توضیحات')

    class Meta:
        verbose_name = 'تجربه'
        verbose_name_plural = 'تجربیات'

    def __str__(self):
        return self.field
class skill(models.Model):
    name = models.CharField('نام', max_length=100)
    percentage = models.IntegerField('درصد')

    class Meta:
        verbose_name = 'مهارت شخصی'
        verbose_name_plural = 'مهارت های شخصی'

    def __str__(self):
        return self.name

class Software_skills(models.Model):
    name = models.CharField('نام', max_length=100)
    percentage = models.IntegerField('درصد')

    class Meta:
        verbose_name = 'مهارت نرم افزاری'
        verbose_name_plural = 'مهارت های نرم افزاری'

    def __str__(self):
        return self.name