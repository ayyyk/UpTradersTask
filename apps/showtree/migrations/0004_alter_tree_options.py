# Generated by Django 4.1.7 on 2023-03-02 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showtree', '0003_tree_full_name_tree_level_alter_tree_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tree',
            options={'ordering': ['full_name']},
        ),
    ]
