# Generated by Django 3.2 on 2021-04-28 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='本文')),
            ],
            options={
                'verbose_name_plural': 'スキルの概要文',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('image', models.ImageField(upload_to='profile', verbose_name='イメージ')),
                ('career', models.CharField(blank=True, max_length=55, null=True, verbose_name='職業')),
                ('org', models.CharField(blank=True, max_length=55, null=True, verbose_name='所属組織')),
                ('age', models.CharField(blank=True, max_length=55, null=True, verbose_name='年齢')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='TwitterのURL')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='FacebookのURL')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='FacebookのURL')),
                ('introduction', models.TextField(verbose_name='自己紹介文')),
            ],
            options={
                'verbose_name_plural': 'プロフィール',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('image', models.ImageField(blank=True, null=True, upload_to='works', verbose_name='イメージ')),
                ('url', models.URLField(verbose_name='URL')),
                ('published', models.DateField(blank=True, null=True, verbose_name='公開日')),
            ],
            options={
                'verbose_name_plural': '作品',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('years', models.FloatField(default=0, verbose_name='経験年数')),
                ('description', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djangostudy.description', verbose_name='説明文')),
            ],
            options={
                'verbose_name_plural': 'スキル',
            },
        ),
    ]
