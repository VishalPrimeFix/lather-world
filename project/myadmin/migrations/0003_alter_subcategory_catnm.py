# Generated by Django 4.0.5 on 2022-07-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_subcategory_alter_category_catnm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='catnm',
            field=models.CharField(max_length=50),
        ),
    ]