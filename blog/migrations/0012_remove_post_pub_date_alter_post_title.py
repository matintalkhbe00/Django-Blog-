# Generated by Django 4.2.7 on 2024-01-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_pub_date_alter_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]
