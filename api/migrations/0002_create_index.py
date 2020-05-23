from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            ('ALTER TABLE api_mentor_profile ADD FULLTEXT (skills)',)
        ),
        migrations.RunSQL(
            ('ALTER TABLE api_userdetails ADD FULLTEXT (description, education)',)
        )
]