from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]+"..."
    def pub_time_better(self):
        return self.pub_date.strftime('%a %d %B %Y')
    def __str__(self):
        return self.title
