# Generated by Django 3.2.5 on 2021-08-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210811_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocerylist',
            name='user',
            field=models.CharField(default='ram1', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grocerylist',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
