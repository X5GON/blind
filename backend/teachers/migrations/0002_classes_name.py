# Generated by Django 2.2.7 on 2020-03-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='name',
            field=models.CharField(default='bla', max_length=150),
            preserve_default=False,
        ),
    ]
