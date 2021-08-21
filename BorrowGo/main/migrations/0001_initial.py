# Generated by Django 3.2.5 on 2021-08-21 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_index', models.IntegerField(null=True)),
                ('commenter', models.CharField(max_length=15)),
                ('cost', models.IntegerField(null=True)),
                ('comment_content', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('writer_id', models.CharField(max_length=10)),
                ('post_title', models.CharField(max_length=30)),
                ('item', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('post_content', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(max_length=15)),
                ('user_name', models.CharField(max_length=6)),
                ('user_nickname', models.CharField(max_length=10)),
                ('user_school', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phonenumber', models.CharField(max_length=15)),
                ('user_favorite', models.TextField()),
                ('confirm', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_borrow', models.IntegerField(default=0)),
                ('start_borrow', models.DateTimeField(null=True)),
                ('end_borrow', models.DateTimeField(null=True)),
                ('is_exceed', models.BooleanField(default=False)),
                ('exceed_time', models.TimeField(null=True)),
                ('exceed_cost', models.IntegerField(null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
    ]