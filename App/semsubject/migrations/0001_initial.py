# Generated by Django 4.0.3 on 2022-03-09 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sem', '0001_initial'),
        ('systemuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semsstudent_Semester', to='sem.semester')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semstudent_User', to='systemuser.systermuser')),
            ],
            options={
                'verbose_name_plural': 'Semstudent',
            },
        ),
    ]
