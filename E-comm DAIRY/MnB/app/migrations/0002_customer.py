# Generated by Django 4.1.6 on 2023-02-18 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('chandigarh', 'chandigarh'), ('dadra & Nagar Haveli', 'dadra & Nagar Haveli'), ('Delhi', 'Delhi'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Utter Pradesh', 'Utter Pradesh'), ('Andra Pradesh', 'Andra Pradesh'), ('Mumbai', 'Mumbai'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
