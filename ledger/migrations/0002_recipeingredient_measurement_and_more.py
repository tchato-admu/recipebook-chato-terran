# Generated by Django 5.0.2 on 2024-03-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='measurement',
            field=models.CharField(default='pc/s', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
