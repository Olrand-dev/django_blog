# Generated by Django 3.0 on 2020-01-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200111_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='entry_type',
            field=models.CharField(default='standard', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='videoarticle',
            name='entry_type',
            field=models.CharField(default='video', editable=False, max_length=50),
        ),
    ]
