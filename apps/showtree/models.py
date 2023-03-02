from django.db import models

class Tree(models.Model):
    tree_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=1000)
    up_elem = models.PositiveBigIntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(default=0)

    class Meta:
        ordering=['full_name']

    def __str__(self):
        return f'{self.name}' # {self.up_elem_name}'


