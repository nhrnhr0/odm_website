# Generated by Django 2.1.5 on 2020-07-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200701_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(upload_to='C:\\Users\\ronio\\OneDrive\\Desktop\\projects\\odm_project\\odm_project\\static\\media_root/', verbose_name='image 2'),
        ),
    ]
