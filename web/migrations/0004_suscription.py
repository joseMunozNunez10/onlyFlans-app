# Generated by Django 3.2.25 on 2024-07-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_suscribed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
