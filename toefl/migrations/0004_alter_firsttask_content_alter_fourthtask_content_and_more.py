# Generated by Django 5.1.4 on 2024-12-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toefl', '0003_remove_sample_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firsttask',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='fourthtask',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='secondtask',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='thirdtask',
            name='content',
            field=models.TextField(),
        ),
    ]