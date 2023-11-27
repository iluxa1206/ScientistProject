from django.db import models
from django.contrib.auth.models import AbstractUser
from disciplines.models import Disciplines


class Student(AbstractUser):
    # Группа - обязательно для заполнения (ограничение по длине в 16 символа)
    group = models.CharField(max_length=16)
    # Курс - обязательно для заполнения
    course = models.SmallIntegerField()
    # Факультет - обязательно для заполнения (ограничение по длине в 255 символа)
    faculty = models.CharField(max_length=255)
    # Дата рождения - обязательно для заполнения
    birthday = models.DateField()
    # Номер телефона - обязательно для заполнения
    phone = models.CharField(max_length=15)

    # Строчки для решения конфликтов при наследовании от одного и того же класса
    groups = models.ManyToManyField('auth.Group', related_name='students')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='student_users')

    # Отображаемое название группы пользователей в админке
    class Meta:
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.first_name + self.last_name


class Scientist(AbstractUser):
    # Биография - необязательна для заполнения
    biography = models.TextField(blank=True)
    # Дата рождения - обязательно для заполнения
    birthday = models.DateField()
    # Должность - обязательно для заполнения (ограничение по длине в 255 символов)
    position = models.CharField(max_length=255)
    # Связь с таблицей "Дисциплины", при удалении дисциплины удаляется упоминание об этой дисциплине
    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE)
    # Ученая степень - обязательно для заполнения (ограничение по длине в 255 символов)
    academic_degree = models.CharField(max_length=255)
    # Фото - необязательно для заполнения, загружается в папку media/scientists
    photo = models.ImageField(upload_to='scientists', blank=True)

    # Строчки для решения конфликтов при наследовании от одного и того же класса
    groups = models.ManyToManyField('auth.Group', related_name='scientists')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='scientist_users')

    # Отображаемое название группы пользователей в админке
    class Meta:
        verbose_name_plural = 'Учёные'

    def __str__(self):
        return self.first_name + self.last_name
