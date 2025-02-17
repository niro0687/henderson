# Generated by Django 4.2.2 on 2023-12-28 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0016_secondinfo_user_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_phone', models.CharField(max_length=200, null=True)),
                ('key_computer', models.CharField(max_length=200, null=True)),
                ('is_phone', models.BooleanField(default=False)),
                ('is_computer', models.BooleanField(default=False)),
                ('android_version', models.CharField(max_length=20)),
                ('android_brand', models.CharField(max_length=20)),
                ('ip_adress', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginTemptation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temptation', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logins', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
