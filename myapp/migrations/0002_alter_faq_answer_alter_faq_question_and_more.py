# Generated by Django 5.1.5 on 2025-02-02 07:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_bn',
            field=models.TextField(blank=True, null=True, verbose_name='Question in Bengali'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_hi',
            field=models.TextField(blank=True, null=True, verbose_name='Question in Hindi'),
        ),
    ]
