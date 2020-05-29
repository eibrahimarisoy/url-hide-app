from django.db import models
from django.contrib.auth.models import User

# Create your models here.
BASE_URL = 'http://localhost:8000/'


class Link(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    exact_link = models.URLField(verbose_name='Asıl Link')
    hide_link = models.URLField(verbose_name='Gizli/Yönlendirilmiş Link')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Linkler'
        ordering = ['created_at']


class ClickCount(models.Model):
    link = models.ForeignKey('Link', on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(verbose_name='Tarih')
    count = models.IntegerField(default=0, verbose_name='Tıklanma Sayısı')

    class Meta:
        verbose_name = 'Link Tıklanma Sayısı'
        verbose_name_plural = 'Linklerin Günlük Tıklanma Sayısı'
        ordering = ['link']
