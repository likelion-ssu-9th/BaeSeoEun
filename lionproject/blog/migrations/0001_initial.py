# Generated by Django 3.2.3 on 2021-05-26 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/')),
            ],
        ),
    ]


#makemigrations데이터베이스스키마와 모델을 맞춰서, 모델을 사용가능하게 만든다.
#스키마=데이터베이스의 구조와 제약조건에 관한 명세들을 기술