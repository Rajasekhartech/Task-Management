# Generated by Django 3.0.3 on 2020-02-24 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskassign', '0006_auto_20200224_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept_assign_task',
            name='status',
            field=models.CharField(choices=[('in_process_dept1', 'in_process_dept1'), ('compleated_dept1', 'compleated_dept1'), ('in_process_dept2', 'in_process_dept2'), ('compleated_dept2', 'compleated_dept2')], max_length=20),
        ),
    ]