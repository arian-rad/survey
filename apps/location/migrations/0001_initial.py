# Generated by Django 4.2.6 on 2023-10-20 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('type', models.CharField(choices=[('country', 'country'), ('city', 'city')], max_length=7, verbose_name='Type')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.location', verbose_name='Country')),
            ],
        ),
    ]
