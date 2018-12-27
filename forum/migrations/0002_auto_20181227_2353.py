# Generated by Django 2.1.4 on 2018-12-27 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forum',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='testcourseforforum',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testcourseforforum',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='testuserforforum',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testuserforforum',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
