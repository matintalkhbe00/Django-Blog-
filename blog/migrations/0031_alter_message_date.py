# Generated by Django 4.2.7 on 2024-02-26 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 26, 14, 47, 23, 222819, tzinfo=datetime.timezone.utc)),
        ),
    ]