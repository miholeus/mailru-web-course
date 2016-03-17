from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(User, related_name='ask_user')
    avatar = models.ImageField(upload_to='users_avatars')
    rating = models.IntegerField()

class Question(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    added_at=models.DateTimeField(auto_now=True, db_index=True)
    rating=models.IntegerField(default=0)
    author=models.ForeignKey(User, related_name='question_author_id')

    likes=models.ManyToManyField(User)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    class Meta:
        db_table = 'questions'
        ordering = ['-added_at']

class Answer(models.Model):
    text=models.TextField()
    added_at=models.DateTimeField(auto_now=True, db_index=True)
    question=models.OneToOneField(Question)
    author=models.ForeignKey(User)

    def __str__(self):
        return self.text
    class Meta:
        db_table = 'answers'
        ordering = ['-added_at']
