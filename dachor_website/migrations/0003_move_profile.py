# Generated by Django 4.1.2 on 2022-10-31 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dachor_website', '0002_birthday_optional'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Profile',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name = 'Profile',
                    table = 'dachor_internal_profile',
                ),
            ]
        ),
    ]

