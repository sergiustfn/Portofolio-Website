# Generated by Django 4.0.1 on 2022-01-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_filesadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]