# Generated by Django 4.1.7 on 2023-03-02 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showtree', '0006_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showtree.menu'),
        ),
        migrations.AddField(
            model_name='tree',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='showtree.tree'),
        ),
    ]