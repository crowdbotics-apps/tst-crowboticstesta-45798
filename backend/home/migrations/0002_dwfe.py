# Generated by Django 3.2.23 on 2024-02-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dwfe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdv', models.BigIntegerField()),
                ('wer', models.CharField(max_length=96)),
            ],
        ),
    ]
