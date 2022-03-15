# Generated by Django 4.0.2 on 2022-03-15 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Search_App', '0002_alter_searchhis_keyword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchhis',
            name='searcher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='searcher', to=settings.AUTH_USER_MODEL),
        ),
    ]
