# Generated by Django 3.0.1 on 2020-05-10 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultydetail', '0006_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='depart_enrolled',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='section_enrolled',
        ),
        migrations.DeleteModel(
            name='year',
        ),
        migrations.RemoveField(
            model_name='extendeduserfaculty',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='extendeduserfaculty',
            name='Section',
        ),
        migrations.RemoveField(
            model_name='extendeduserfaculty',
            name='Year',
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.DeleteModel(
            name='section',
        ),
        migrations.DeleteModel(
            name='subject',
        ),
    ]
