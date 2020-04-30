# Generated by Django 3.0.5 on 2020-04-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavod', '0010_zavodnik'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zavodnik',
            options={'ordering': ['-datum_narozeni', 'prijmeni']},
        ),
        migrations.AddField(
            model_name='zavodnik',
            name='datum_narozeni',
            field=models.DateField(blank=True, null=True, verbose_name='Datum narozeni'),
        ),
        migrations.AddField(
            model_name='zavodnik',
            name='kariera',
            field=models.TextField(blank=True, null=True, verbose_name='Kariera'),
        ),
        migrations.AddField(
            model_name='zavodnik',
            name='klub',
            field=models.ManyToManyField(help_text='Vyber svůj klub', to='zavod.klub'),
        ),
        migrations.AddField(
            model_name='zavodnik',
            name='prijmeni',
            field=models.CharField(max_length=45, null=True, verbose_name='Prijmeni zavodnika'),
        ),
    ]
