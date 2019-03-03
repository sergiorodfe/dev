# Generated by Django 2.1.5 on 2019-02-04 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myroot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=75, unique=True)),
                ('property_value', models.CharField(blank=True, max_length=254, null=True)),
                ('property_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('property_group', models.CharField(choices=[('APP_CONF', 'App Setting'), ('GENERAL_CONF', 'General Setting'), ('PROHIBITED_USER_NAME', 'Prohibited User Name'), ('PROHIBITED_USER_EMAIL', 'Prohibited User Email'), ('OTHERS', 'Other')], default='APPSETTING', max_length=75)),
            ],
            options={
                'verbose_name': 'Site Config',
                'verbose_name_plural': 'Site Configs',
                'db_table': 'dev_site_config',
            },
        ),
        migrations.AlterIndexTogether(
            name='siteconfig',
            index_together={('property_group',)},
        ),
    ]
