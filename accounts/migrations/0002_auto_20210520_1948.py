# Generated by Django 3.1.7 on 2021-05-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='num',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='t_num',
        ),
        migrations.AddField(
            model_name='accounts',
            name='address',
            field=models.TextField(default='bkreddy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accounts',
            name='email',
            field=models.CharField(default='bsree@gmail.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accounts',
            name='name',
            field=models.CharField(default='bhanu', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accounts',
            name='number',
            field=models.CharField(default='sree', max_length=50),
            preserve_default=False,
        ),
    ]
