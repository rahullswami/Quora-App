# Generated by Django 4.2.16 on 2024-12-30 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_alter_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('question_posted', 'Question Posted')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]