# Generated by Django 4.0.4 on 2022-04-22 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_ethnos_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=255)),
                ('body', models.TextField(verbose_name='')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
