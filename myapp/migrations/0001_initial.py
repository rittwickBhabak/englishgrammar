# Generated by Django 3.2.6 on 2021-08-23 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slno', models.IntegerField()),
                ('static_folder', models.SlugField()),
                ('total_pages', models.IntegerField()),
                ('last_read_page', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1000)),
                ('page_number', models.IntegerField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.chapter')),
            ],
        ),
    ]
