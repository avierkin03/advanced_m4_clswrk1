from django.db import models
from django.utils import timezone
from datetime import timedelta

# Визначення моделей, які Django використовує для створення схеми бази даних
class Author(models.Model):
    name = models.CharField(max_length=255) 
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='posts')

    def published_recently(self):
        if not self.published_date:
            return False
        # timezone.now() повертає поточну дату та час у часовій зоні, яка налаштована в Django.
        # timedelta(days=7) створює інтервал у 7 днів.
        #self.published_date >= timezone.now() - timedelta(days=7) перевіряє, чи published_date не старше 7 днів від поточної дати.
        return self.published_date >= timezone.now() - timedelta(days=7)

    def __str__(self):
        return self.title
    