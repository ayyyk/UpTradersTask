# Generated by Django 4.1.7 on 2023-03-03 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showtree', '0007_tree_menu_tree_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showtree.menu'),
        ),
    ]
