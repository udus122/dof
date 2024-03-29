# Generated by Django 2.2.10 on 2020-03-21 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dof', '0003_diagnosisresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosisresult',
            name='thinking_order',
            field=models.TextField(default='', verbose_name='思考の順番'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diagnosisresult',
            name='advice',
            field=models.TextField(blank=True, default='', null=True, verbose_name='アドバイス'),
        ),
        migrations.AlterField(
            model_name='diagnosisresult',
            name='strength',
            field=models.TextField(blank=True, default='', null=True, verbose_name='強み'),
        ),
        migrations.AlterField(
            model_name='diagnosisresult',
            name='stressor',
            field=models.TextField(blank=True, default='', null=True, verbose_name='ストレス要因'),
        ),
        migrations.AlterField(
            model_name='diagnosisresult',
            name='weakness',
            field=models.TextField(blank=True, default='', null=True, verbose_name='弱み'),
        ),
    ]
