# Generated by Django 3.0 on 2020-01-11 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='country')),
                ('state', models.CharField(blank=True, max_length=150, verbose_name='state')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='city')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='category name')),
                ('desc', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='publication date')),
                ('header', models.CharField(max_length=150, verbose_name='header')),
                ('text', models.TextField(verbose_name='text')),
                ('image_thumb', models.ImageField(blank=True, upload_to='articles/thumbs/', verbose_name='thumbnail image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Category')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='SpecialEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='publication date')),
                ('header', models.CharField(max_length=150, verbose_name='header')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Category')),
            ],
            options={
                'verbose_name_plural': 'special entries',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='tag name')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('entry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Entry')),
                ('image', models.ImageField(blank=True, upload_to='articles/full-images/', verbose_name='full image')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.entry',),
        ),
        migrations.CreateModel(
            name='LinkEntry',
            fields=[
                ('specialentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.SpecialEntry')),
                ('desc', models.CharField(blank=True, max_length=150, verbose_name='link description')),
                ('url', models.CharField(max_length=200, verbose_name='link')),
            ],
            options={
                'verbose_name_plural': 'link entries',
            },
            bases=('base.specialentry',),
        ),
        migrations.CreateModel(
            name='QuoteEntry',
            fields=[
                ('specialentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.SpecialEntry')),
                ('text', models.TextField(verbose_name='text')),
                ('cite', models.CharField(max_length=50, verbose_name='cite')),
            ],
            options={
                'verbose_name_plural': 'quote entries',
            },
            bases=('base.specialentry',),
        ),
        migrations.CreateModel(
            name='VideoArticle',
            fields=[
                ('entry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Entry')),
                ('video_url', models.CharField(max_length=200, verbose_name='video link')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.entry',),
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='base.Tag'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='publication date')),
                ('text', models.TextField(verbose_name='text')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Author')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Entry')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', related_query_name='reply', to='base.Comment')),
            ],
        ),
    ]