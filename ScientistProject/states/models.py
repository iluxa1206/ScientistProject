from django.db import models
from users.models import Scientist


class State(models.Model):
    # Название - обязательно для заполнения (ограничение по длине в 255 символов)
    title = models.CharField(max_length=255)
    # Текст статьи - необязательна для заполнения
    text = models.TextField()
    # Связь с таблицей "Учёные", при удалении учёного удаляется упоминание об этом учёном
    scientist_tag = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    # Фото для превью - необязательно для заполнения, загружается в папку media/states
    photo = models.ImageField(upload_to='states')

    # Отображаемое название группы пользователей в админке
    class Meta:
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
