# Generated by Django 3.0.5 on 2020-04-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='klub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Enter a nazev klubu', max_length=50, unique=True, verbose_name='Nazev klubu')),
            ],
        ),
    ]