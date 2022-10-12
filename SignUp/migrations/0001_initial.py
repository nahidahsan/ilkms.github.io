# Generated by Django 4.1.1 on 2022-09-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                ("gender", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=64)),
                ("password2", models.CharField(max_length=64)),
            ],
            options={"db_table": "users",},
        ),
    ]
