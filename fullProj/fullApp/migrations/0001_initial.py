# Generated by Django 3.0.8 on 2020-07-05 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name_of_action', models.CharField(max_length=50)),
                ('Action_startTime', models.DateTimeField(default=None, null=True)),
                ('Action_endTime', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Real_Name', models.CharField(max_length=100)),
                ('Tz', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MappTable',
            fields=[
                ('activity_mapping_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullApp.Activity')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullApp.User1')),
            ],
        ),
    ]
