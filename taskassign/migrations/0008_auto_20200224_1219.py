# Generated by Django 3.0.3 on 2020-02-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskassign', '0007_auto_20200224_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(default='inactive', max_length=20),
        ),
    ]
