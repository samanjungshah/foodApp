# Generated by Django 3.2.5 on 2022-08-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.CharField(default='https://www.food4fuel.com/wp-content/uploads/woocommerce-placeholder-600x600.png', max_length=500),
        ),
    ]