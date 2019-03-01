from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Raccoon(models.Model):
    name = models.CharField(max_length=255,verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")
    parent = models.ForeignKey('Raccoon',blank=True,null=True, verbose_name="Родитель")
    avatar = models.ImageField(blank=True,null=True, verbose_name="Аватар")
    class Meta:
        verbose_name='Енот'
        verbose_name_plural='Еноты'
        permissions=(('can_be','can be'),)

    def admin_t(self):
        return mark_safe(u'<img src="%s" style="height:100px">' %self.avatar.url)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Photo(models.Model):
    img = models.ImageField()
    raccoon = models.ForeignKey(Raccoon, verbose_name="Енот")
    description = models.TextField(blank=True, verbose_name="Описание")
    class Meta:
        verbose_name='Фотография енота'
        verbose_name_plural='Фотографии енотов'

