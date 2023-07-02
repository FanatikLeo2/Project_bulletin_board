from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('trader', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('questgiver', 'Квестгиверы'),
        ('blacksmith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potionmaster', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=12, choices=TYPE, default='tank')
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'{self.title}'


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.IntegerField(choices=((0, 'Not considered'), (1, 'Accept'), (2, 'Reject')), default=0,)

    def __str__(self):
        return f'{self.text}  ----   {self.post}'

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'
