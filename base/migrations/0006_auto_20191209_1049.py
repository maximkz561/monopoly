# Generated by Django 3.0 on 2019-12-09 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20191208_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.Room'),
        ),
    ]
