# Generated by Django 4.1.7 on 2023-03-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtree', '0015_rename_link_name_tree_named_url_rename_link_tree_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='url',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]