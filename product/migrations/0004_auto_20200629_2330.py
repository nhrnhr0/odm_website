# Generated by Django 2.1.5 on 2020-06-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_merge_20200629_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='C:\\Users\\ronio\\OneDrive\\Desktop\\projects\\odm_project\\odm_project\\upload/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='no name', max_length=120, verbose_name='name'),
        ),
    ]