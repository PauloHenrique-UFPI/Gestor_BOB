# Generated by Django 3.0 on 2022-05-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_auto_20220417_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=120, unique=True, verbose_name='Titulo do livro'),
        ),
    ]
