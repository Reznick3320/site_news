# Generated by Django 3.2.7 on 2021-10-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20211005_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='short_descr',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
