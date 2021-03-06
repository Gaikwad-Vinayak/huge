# Generated by Django 4.0.6 on 2022-07-06 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation_Mst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designaton', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Mst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.EmailField(max_length=254)),
                ('date_of_joining', models.DateField()),
                ('salary', models.FloatField()),
                ('designationld', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.designation_mst')),
            ],
        ),
        migrations.DeleteModel(
            name='mode',
        ),
    ]
