# Generated by Django 4.2.7 on 2024-02-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_message_created_message_date_message_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='date',
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
