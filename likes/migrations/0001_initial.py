# Generated by Django 4.0 on 2023-04-20 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('account', '0005_alter_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateliked', models.DateTimeField(auto_created=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_post', to='posts.blogpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_post_liked', to='account.customuser')),
            ],
            options={
                'ordering': ['-dateliked'],
            },
        ),
        migrations.AddIndex(
            model_name='likes',
            index=models.Index(fields=['user', 'post', 'id'], name='likes_likes_user_id_a76a36_idx'),
        ),
    ]
