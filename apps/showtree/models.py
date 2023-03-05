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
    link = models.CharField(max_length=2048)

    class Meta:
        ordering=['-menu', 'parent_id', 'name']

    def __str__(self):
        return f'{self.name} ({self.id})'

    # def get_absolute_url(self, pk):
    #     return reverse(self.url)


