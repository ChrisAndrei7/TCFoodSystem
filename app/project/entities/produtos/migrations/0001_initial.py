# Generated by Django 4.2.1 on 2024-01-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.CharField(max_length=250)),
                ('ingredientes', models.CharField(max_length=250)),
                ('categoria', models.CharField(max_length=250)),
                ('preco', models.FloatField()),
            ],
        ),
    ]
