# Generated by Django 4.2.4 on 2023-09-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0006_delete_customgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Permission_user',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Manger', 'Manger'), ('User', 'User')], default='User', max_length=50),
        ),
    ]