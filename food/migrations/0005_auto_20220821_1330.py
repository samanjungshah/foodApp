# Generated by Django 3.2.5 on 2022-08-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20220821_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteminstance',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_name',
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ItemName',
        ),
    ]
