# Generated by Django 3.2.9 on 2022-02-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='decoded_image.jpg', upload_to='images/'),
        ),
    ]
