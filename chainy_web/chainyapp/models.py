from django.db import models

class Chain(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    chain = models.ForeignKey(Chain)
    post_num = models.IntegerField()
    poster = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.body
