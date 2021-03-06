# Generated by Django 2.2.16 on 2020-12-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=100)),
                ('employment', models.CharField(max_length=100)),
                ('pregnancy', models.CharField(max_length=100)),
                ('diet', models.CharField(max_length=100)),
                ('first_food', models.CharField(max_length=100)),
                ('second_food', models.CharField(max_length=100)),
                ('third_food', models.CharField(max_length=100)),
                ('fourth_food', models.CharField(max_length=100)),
                ('fifth_food', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
