# Generated by Django 4.1 on 2022-10-16 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosen', '0002_remove_dosen_alamat_rumah_remove_dosen_fakultas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosen',
            name='foto',
        ),
        migrations.AddField(
            model_name='dosen',
            name='jabatan',
            field=models.CharField(max_length=200, null=True),
        ),
    ]