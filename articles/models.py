from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    pub_date = models.DateTimeField()
    body = models.TextField()

    def summary(self):
        return ' '.join(self.body.split()[:20]) + '...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# Create your models here.
