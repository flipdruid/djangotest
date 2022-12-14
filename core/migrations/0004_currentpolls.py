# Generated by Django 4.1.1 on 2022-09-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_title_core_poll_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currentpolls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentUser', models.CharField(max_length=20)),
                ('pollID', models.IntegerField(default=0)),
                ('pollComments', models.CharField(max_length=200)),
                ('commentsDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
