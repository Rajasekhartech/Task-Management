# Generated by Django 3.0.3 on 2020-02-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskassign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
