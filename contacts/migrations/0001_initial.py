# Generated by Django 4.0 on 2023-06-25 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='login_user', to='account.customuser')),
                ('user_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_friend', to='account.customuser')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['-created', 'user_to'], name='contacts_co_created_baeaa0_idx'),
        ),
    ]
