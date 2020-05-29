# Generated by Django 2.1 on 2020-05-26 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('on_demand', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            ('ALTER TABLE on_demand_supplier_profile ADD FULLTEXT (skills)',)
        ),
        migrations.RunSQL(
            ('ALTER TABLE on_demand_userdetails ADD FULLTEXT (description, education)',)
        )
    ]