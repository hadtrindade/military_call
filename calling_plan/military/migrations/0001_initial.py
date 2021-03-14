# Generated by Django 3.1.7 on 2021-03-13 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Area",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "area",
                    models.CharField(
                        choices=[
                            ("S", "Sul"),
                            ("N", "Norte"),
                            ("L", "Leste"),
                            ("O", "Oeste"),
                            ("G", "Guarnição"),
                            ("F", "Fora da Guarnição"),
                        ],
                        max_length=1,
                        verbose_name="Área",
                    ),
                ),
                (
                    "descricao",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Descrição"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PostoGraduacao",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=20, unique=True)),
                ("sigla", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SubUnidade",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("sigla", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Militares",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("identidade", models.CharField(max_length=11)),
                ("nome", models.CharField(max_length=200)),
                (
                    "operacional",
                    models.BooleanField(verbose_name="Operacional"),
                ),
                ("telefone", models.CharField(max_length=20)),
                (
                    "telefone_familia",
                    models.CharField(
                        max_length=20, verbose_name="Telefone de Familiar"
                    ),
                ),
                (
                    "telefone_telegram",
                    models.CharField(max_length=20, verbose_name="Telegram"),
                ),
                (
                    "telefone_whatsapp",
                    models.CharField(max_length=20, verbose_name="Whatsapp"),
                ),
                ("chamador", models.BooleanField(verbose_name="Chamador")),
                ("rua", models.CharField(max_length=200)),
                ("bairro", models.CharField(max_length=100)),
                ("cidade", models.CharField(max_length=100)),
                (
                    "estado",
                    models.CharField(max_length=100, verbose_name="UF"),
                ),
                ("cep", models.IntegerField()),
                ("data_insercao", models.DateField(auto_now_add=True)),
                (
                    "area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="military.area",
                        verbose_name="Área",
                    ),
                ),
                (
                    "graduacao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="military.postograduacao",
                        verbose_name="Posto/Graduação",
                    ),
                ),
                (
                    "subunidade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="military.subunidade",
                        verbose_name="Subunidade",
                    ),
                ),
            ],
        ),
    ]