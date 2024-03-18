from django.db import models


class Disciplines(models.Model):
    # Название - обязательно для заполнения (ограничение по длине в 255 символов)
    name = models.CharField(max_length=255)
    # Описание - необязательна для заполнения
    description = models.TextField(blank=True)

    # Отображаемое название группы пользователей в админке
    class Meta:
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.name


class Tag(models.Model):
    # Название - обязательно для заполнения (ограничение по длине в 64 символов)
    name = models.CharField(max_length=64)
    # Связь с таблицей "Статьи", при удалении статьи удаляется тэг для этой статьи
    state = models.ForeignKey('states.State', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
