# Generated by Django 4.2.1 on 2023-05-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registro_de_animais", "0002_rename_name_animal_nome_alter_animal_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tutor",
            name="nome",
        ),
        migrations.AlterField(
            model_name="animal",
            name="especie",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="animal",
            name="porte",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="animal",
            name="raça",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="animal",
            name="sexo",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="animal",
            name="tutor",
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name="Especie",
        ),
        migrations.DeleteModel(
            name="Porte",
        ),
        migrations.DeleteModel(
            name="Raça",
        ),
        migrations.DeleteModel(
            name="Sexo",
        ),
        migrations.DeleteModel(
            name="Tutor",
        ),
    ]
