# Generated by Django 4.2.7 on 2024-01-21 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default.png', upload_to='post/'),
        ),
    ]
