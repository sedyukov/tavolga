from django.db import models
from ckeditor.fields import RichTextField


class Authors(models.Model):
    photo = models.ImageField(upload_to='main/static/img/', verbose_name='Фото')
    name = models.CharField(max_length=50, verbose_name='Имя')
    soname = models.CharField(max_length=50, verbose_name='Фамилия')
    bio = RichTextField(null=True, blank=True, verbose_name='Биография')
    draft = models.BooleanField(verbose_name='Черновик', default=False)

    def __str__(self):
        return f'{self.name} {self.soname}'

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'
        ordering = ['-soname']

    def link_draft(self):
        return f'http://127.0.0.1:8000/mag/maglast/{self.id}/draft/'


class Number(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='main/static/img/', verbose_name='Обложка')
    name = models.CharField(max_length=50, verbose_name='Название номера')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создан')
    draft = models.BooleanField(verbose_name='Черновик', default=True)

    def __str__(self):
        s = self.name
        return s

    def link_draft(self):
        return f'http://127.0.0.1:8000/mag/maglast/{self.id}/draft/'

    class Meta:
        verbose_name_plural = 'Номера'
        verbose_name = 'Номер'
        ordering = ['-name']


class Material(models.Model):
    name = models.CharField(max_length=50, verbose_name='Оглавление материала')
    text = RichTextField(null=True, blank=True, verbose_name='Текст')
    auth = models.ForeignKey('Authors', null=True, on_delete=models.PROTECT, related_name='number', verbose_name='Автор')
    number = models.ForeignKey('Number', null=True, on_delete=models.PROTECT, related_name='number', verbose_name='Номер')
    spell = models.CharField(max_length=50, verbose_name='Порядоковый номер автора в номере')
    draft = models.BooleanField(verbose_name='Черновик', default=False)

    def get_auth(self):
        return self.auth

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Материалы'
        verbose_name = 'Материал'
        ordering = ['-spell']


class News(models.Model):
    name = models.CharField(max_length=50, verbose_name='Заголовок новости')
    text = RichTextField(null=True, blank=True, verbose_name='Текст')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создан')
    draft = models.BooleanField(verbose_name='Черновик', default=False)

    def __str__(self):
        return self.name

    def link_draft(self):
        return f'http://127.0.0.1:8000/mag/maglast/{self.id}/draft/'

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-published']


class Contacts(models.Model):
    about = RichTextField(null=True, blank=True, verbose_name='Текст')
    vk = models.CharField(null=True, blank=True, max_length=50, verbose_name='vk')
    tg = models.CharField(null=True, blank=True, max_length=50, verbose_name='tg')
    fb = models.CharField(null=True, blank=True, max_length=50, verbose_name='fb')
    inst = models.CharField(null=True, blank=True, max_length=50, verbose_name='instagram')

    def __str__(self):
        return 'Контакты'

    def link_draft(self):
        return f'http://127.0.0.1:8000/mag/maglast/{self.id}/draft/'

    class Meta:
        verbose_name_plural = 'Контакт'
        verbose_name = 'Контакты'
