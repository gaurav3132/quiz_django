# Generated by Django 3.1.1 on 2020-11-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('option1', models.CharField(max_length=20)),
                ('option2', models.CharField(max_length=20)),
                ('option3', models.CharField(max_length=20)),
                ('option4', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=20)),
            ],
        ),
    ]
