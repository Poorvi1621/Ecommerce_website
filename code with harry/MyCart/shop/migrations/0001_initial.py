# Generated by Django 4.1.3 on 2023-01-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('Desc', models.CharField(max_length=300)),
                ('price', models.IntegerField(default='0')),
                ('category', models.CharField(max_length=50)),
                ('subcategory', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='shop/images')),
            ],
        ),
    ]