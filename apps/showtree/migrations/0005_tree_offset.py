# Generated by Django 4.1.7 on 2023-03-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtree', '0004_alter_tree_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='offset',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
