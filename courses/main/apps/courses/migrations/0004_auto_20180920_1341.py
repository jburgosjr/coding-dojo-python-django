# Generated by Django 2.1.1 on 2018-09-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180920_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='courses_comment',
        ),
        migrations.RemoveField(
            model_name='description',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]