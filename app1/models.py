from django.db import models

class Project(models.Model):
    title = models.CharField(default='', max_length=250)
    description = models.TextField()
    demo_link = models.CharField(max_length=250)
    tags = models.ManyToManyField('Tags', blank=True)
    source_code = models.CharField(max_length=250,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    VOTE_CHOICES = [
        ('up','up vote'),
        ('down','down vote'),
    ]
    description = models.TextField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    values = models.CharField(max_length=200, choices=VOTE_CHOICES)

    def __str__(self) -> str:
        return self.values

class Tags(models.Model):
    title = models.CharField(default='', max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
