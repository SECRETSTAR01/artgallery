# Generated by Django 3.1.3 on 2021-06-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_work', models.ImageField(upload_to='arts/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
