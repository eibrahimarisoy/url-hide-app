import random
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    exact_link = models.URLField(verbose_name='URL giriniz.')
    slug = models.SlugField(blank=True, null=True, unique=True)
    hide_link = models.CharField(
        max_length=255,
        verbose_name='Gizli/Yönlendirilmiş Link',
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Linkler'
        ordering = ['-created_at']
        unique_together = ('owner', 'exact_link')

    def __str__(self):
        return f"{self.exact_link} >> {self.hide_link}"

    def random_string(self, stringLength=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def save(self, *args, **kwargs):
        random_string = self.random_string()
        BASE_URL = settings.BASE_URL
        self.slug = random_string
        self.hide_link = f"{BASE_URL}{self.slug}"
        super(Link, self).save(*args, **kwargs)


class Click(models.Model):
    link = models.ForeignKey(
        'Link',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        unique_for_date="date"
    )
    date = models.DateField(verbose_name='Tarih')
    count = models.IntegerField(
        default=0,
        verbose_name='Tıklanma Sayısı')

    class Meta:
        verbose_name = 'Link Tıklanma Sayısı'
        verbose_name_plural = 'Linklerin Günlük Tıklanma Sayısı'
        ordering = ['link']

    def __str__(self):
        return f"{self.link} >> {self.date} >> {self.count}"


class Browser(models.Model):
    link = models.ForeignKey(
        'Link',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    click_time = models.DateTimeField()

    class Meta:
        ordering = ['link']

    def __str__(self):
        return f"{self.name} >> {self.link} >> {self.click_time}"


class OperatingSystem(models.Model):
    link = models.ForeignKey(
        'Link',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    click_time = models.DateTimeField()

    class Meta:
        ordering = ['link']

    def __str__(self):
        return f"{self.name} >> {self.link} >> {self.click_time}"
