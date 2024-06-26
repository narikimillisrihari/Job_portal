# Generated by Django 3.2.24 on 2024-06-24 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('age', models.IntegerField()),
                ('expect_salary', models.IntegerField()),
                ('resume_url', models.URLField(max_length=250)),
                ('progress', models.CharField(choices=[('applied', 'Applied'), ('shortlisted', 'Shortlisted'), ('selected', 'Selected')], default='applied', max_length=20)),
                ('apply_date', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job_model')),
            ],
        ),
    ]
