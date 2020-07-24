# Generated by Django 3.0.8 on 2020-07-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='', max_length=255)),
                ('category', models.CharField(default='', max_length=50)),
                ('price', models.PositiveIntegerField(default=100)),
                ('was_included_in_home', models.BooleanField(default=False)),
            ],
        ),
    ]
