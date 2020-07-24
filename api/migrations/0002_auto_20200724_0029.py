# Generated by Django 3.0.8 on 2020-07-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toymodel',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='toymodel',
            name='category',
            field=models.CharField(default='Something', max_length=50),
        ),
        migrations.AlterField(
            model_name='toymodel',
            name='description',
            field=models.TextField(default='Something', max_length=255),
        ),
        migrations.AlterField(
            model_name='toymodel',
            name='name',
            field=models.CharField(default='Something', max_length=50),
        ),
    ]
