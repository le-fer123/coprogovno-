from django.db import models


class FirstTask(models.Model):
    preparation = models.IntegerField(default=15)
    speach = models.IntegerField(default=45)
    content = models.TextField()

    def __str__(self):
        return f'{self.content[:5]} id: {self.id}'


class SecondTask(models.Model):
    preparation = models.IntegerField(default=30)
    reading = models.IntegerField(default=40)
    speach = models.IntegerField(default=60)
    content = models.TextField()

    def __str__(self):
        return f'{self.content[:5]} id: {self.id}'


class ThirdTask(models.Model):
    preparation = models.IntegerField(default=30)
    reading = models.IntegerField(default=45)
    speach = models.IntegerField(default=60)
    content = models.TextField()

    def __str__(self):
        return f'{self.content[:5]} id: {self.id}'


class FourthTask(models.Model):
    preparation = models.IntegerField(default=20)
    speach = models.IntegerField(default=60)
    content = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to='toefl/audio')

    def __str__(self):
        return f'{self.content[:5]} id: {self.id}'


class Sample(models.Model):
    first = models.ForeignKey(to=FirstTask, on_delete=models.CASCADE)
    second = models.ForeignKey(to=SecondTask, on_delete=models.CASCADE)
    third = models.ForeignKey(to=ThirdTask, on_delete=models.CASCADE)
    fourth = models.ForeignKey(to=FourthTask, on_delete=models.CASCADE)

    def __str__(self):
        return f'toefl id {self.id}'
