# Generated by Django 2.1.5 on 2020-03-19 10:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=20)),
                ('hobby', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(upload_to='image')),
                ('status', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=128)),
                ('relationship_status', models.CharField(choices=[('singale', 'Singale'), ('marrid', 'Marrid')], max_length=128)),
                ('phone', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]