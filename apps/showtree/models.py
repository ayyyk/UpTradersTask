from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering=['name']

    def __str__(self):
        return f'{self.name}'


class Tree(models.Model):
    tree_name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', 
                                on_delete=models.CASCADE,
                                blank=True, null=True,
                                related_name='childs')
    name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=1000)
    up_elem = models.PositiveBigIntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(default=0)
    offset = models.PositiveIntegerField(default=0)

    class Meta:
        ordering=['full_name']

    def __str__(self):
        return f'{self.name}'


