from django.db import models

# Create your models here.

class Game(models.Model):
    Opponent = models.ForeignKey('Opponent', on_delete=models.RESTRICT, verbose_name="Оппонент")
    Game_day = models.DateTimeField(null=True, blank=True, verbose_name="Дата и Время игры")
    Goals = models.SmallIntegerField(default=0, verbose_name="Наши голы")
    Opponent_goals = models.SmallIntegerField(default=0, verbose_name="Голы Оппонента")


class Player(models.Model):
    Firstname = models.CharField(max_length=255, verbose_name='Имя')
    Lastname = models.CharField(max_length=255, verbose_name='Фамилия')
    Patronymic = models.CharField(max_length=255, null=True, blank=True, verbose_name='Отчество')
    Phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Контактный Номер')
    Age = models.SmallIntegerField(verbose_name='Возраст')
    isActive = models.BooleanField(default=True, verbose_name="Активный")
    PlayNumber = models.SmallIntegerField(null=True, blank=True, default=-1, verbose_name="Игровой Номер игрока")
    Team = models.ForeignKey('Team', on_delete=models.RESTRICT)


class Team(models.Model):
    Name = models.CharField(max_length=255, verbose_name='Название')


class Tourney(models.Model):
    Name = models.CharField(max_length=255, verbose_name='Название')
    Start_dt = models.DateField(verbose_name="Начало")
    Stop_dt = models.DateField(verbose_name="Конец", null=True, blank=True)
    IsComplete = models.BooleanField(default=False,verbose_name="Завершен")

class Opponent(models.Model):
    Name = models.CharField(max_length=255, verbose_name='Название')


class Result(models.Model):
    Game =models.ForeignKey('Game', on_delete=models.RESTRICT, verbose_name="Игры")
    Player =models.ForeignKey('Player', on_delete=models.RESTRICT, verbose_name="Игрок")
    Goals = models.SmallIntegerField(verbose_name="Колчество голов")

class Card(models.Model):
    Yellow = 'Y'
    Red = 'R'
    CARDS = [
        (Yellow, 'Yellow'),
        (Red, 'Red')
    ]
    
    card = models.CharField(max_length=2,choices=CARDS, default=Yellow, verbose_name="Каточка")

class WorkoutDay(models.Model):
    dt_workout = models.DateField(auto_created=True, verbose_name="Дата Тренировки")
    Enable =models.BooleanField(default=True, verbose_name="Состоялась")

class WorkoutSkip(models.Model):
    Player = models.ForeignKey('Player', on_delete=models.CASCADE)
    attandend =models.BooleanField(default=True, verbose_name="Присутвовал")
    cause = models.ForeignKey('CauseSkip', on_delete=models.RESTRICT, verbose_name="Причина Пропуска")

class CauseSkip(models.Model):
    value = models.CharField(max_length=100, verbose_name='Причина пропуска')