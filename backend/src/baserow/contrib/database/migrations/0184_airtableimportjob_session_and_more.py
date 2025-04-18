# Generated by Django 5.0.9 on 2025-03-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0183_viewgroupby_type_viewsort_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="airtableimportjob",
            name="session",
            field=models.CharField(
                help_text="Optionally provide a session object that's used as authentication.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="airtableimportjob",
            name="session_signature",
            field=models.CharField(
                help_text="The matching session signature if a session is provided.",
                null=True,
            ),
        ),
    ]
