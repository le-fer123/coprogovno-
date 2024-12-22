from django.db import models


class FirstPart(models.Model):
    duration = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f'{self.content[:5]}, id={self.id}'

class SecondPart(models.Model):
    duration = models.IntegerField()
    content = models.TextField()
    followup = models.TextField()

    def __str__(self):
        return f'{self.content[:5]}, id={self.id}'

class ThirdPart(models.Model):
    duration = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f'{self.content[:5]}, id={self.id}'

class Sample(models.Model):
    first = models.ForeignKey(to=FirstPart, on_delete=models.CASCADE)
    second = models.ForeignKey(to=SecondPart, on_delete=models.CASCADE)
    third = models.ForeignKey(to=ThirdPart, on_delete=models.CASCADE)

    def __str__(self):
        return f'ielts {self.id}'


