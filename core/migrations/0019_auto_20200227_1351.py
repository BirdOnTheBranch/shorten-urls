# Generated by Django 3.0.2 on 2020-02-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200225_1900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-create'], 'verbose_name': 'link', 'verbose_name_plural': 'links'},
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(),
        ),
    ]