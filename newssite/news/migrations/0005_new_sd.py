# Generated by Django 3.2.7 on 2021-10-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_fist_name_author_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='sd',
            field=models.CharField(default=1, max_length=47),
            preserve_default=False,
        ),
    ]
