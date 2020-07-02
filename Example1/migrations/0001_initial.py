# Generated by Django 2.2.7 on 2020-07-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('edad', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('curp', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'Example1',
            },
        ),
    ]