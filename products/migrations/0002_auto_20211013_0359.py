# Generated by Django 3.2.7 on 2021-10-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='price',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='rate',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='rate'),
        ),
    ]