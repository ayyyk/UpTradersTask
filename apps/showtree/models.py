from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering=['name']

    def __str__(self):
        return f'{self.name}'


class Tree(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', 
                                on_delete=models.CASCADE,
                                blank=True, null=True,
                                related_name='childs')
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=2048, blank=True, null=True)
    named_url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering=['menu', 'parent_id', 'name']

    def clean(self):
        if self.url:
            if self.named_url:
                raise ValidationError(
                    'One of that fields must be blank (url, named_url)')
            while self.url.startswith('/'):
                self.url = self.url[1:]
            while self.url.endswith('/'):
                self.url = self.url[:-1]

    def __str__(self):
        return f'{self.name} ({self.id})'