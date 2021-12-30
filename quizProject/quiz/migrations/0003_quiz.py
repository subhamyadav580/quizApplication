# Generated by Django 4.0 on 2021-12-30 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='quiz.user')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='quiz.subject')),
            ],
        ),
    ]
