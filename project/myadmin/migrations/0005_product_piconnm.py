# Generated by Django 4.0.4 on 2022-07-22 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='piconnm',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
