from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}  email"{self.mail}'

    class Meta:
        verbose_name_plural = 'Author'


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = 'Tags'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True, unique=True)
    content = models.TextField()
    objects = models.Manager()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title}, {self.author}, {self.date}'

    class Meta:
        verbose_name_plural = 'Posts'