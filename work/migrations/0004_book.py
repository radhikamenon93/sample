# Generated by Django 4.2.6 on 2023-11-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('year', models.PositiveIntegerField()),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
    ]
