# Generated by Django 5.0.4 on 2024-06-24 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discapacidad', '0005_tramabasediscapacidadrpt05rbcnominal_casos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadPOI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(verbose_name='Año')),
                ('tipo_presupuesto', models.CharField(choices=[('PIA', 'PIA'), ('PIM', 'PIM')], max_length=3)),
                ('fecha_registro', models.DateField()),
                ('pliego', models.CharField(max_length=255)),
                ('unidad_ejecutora', models.CharField(max_length=255)),
                ('objetivo_sectorial', models.CharField(blank=True, max_length=255, null=True, verbose_name='Objetivo Sectorial/PESEM')),
                ('objetivo_institucional', models.CharField(blank=True, max_length=255, null=True, verbose_name='Objetivo Institucional/PEI')),
                ('accion_estrategica', models.CharField(blank=True, max_length=255, null=True, verbose_name='Acción Estratégica/PEI')),
                ('tipo_categoria', models.CharField(blank=True, choices=[('PpR', 'PpR'), ('APNOP', 'APNOP')], max_length=10, null=True)),
                ('categoria_presupuestal', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_producto_proyecto', models.CharField(blank=True, choices=[('Producto', 'Producto'), ('Proyecto', 'Proyecto')], max_length=20, null=True)),
                ('producto_presupuestal', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_actividad_obra', models.CharField(blank=True, max_length=255, null=True)),
                ('actividad_presupuestal', models.CharField(blank=True, max_length=255, null=True)),
                ('funcion', models.CharField(blank=True, max_length=255, null=True)),
                ('division_funcional', models.CharField(blank=True, max_length=255, null=True)),
                ('grupo_funcional', models.CharField(blank=True, max_length=255, null=True)),
                ('actividad_operativa', models.CharField(blank=True, max_length=255, null=True)),
                ('unidad_medida', models.CharField(blank=True, choices=[('Informes', 'Informes'), ('Reportes', 'Reportes')], max_length=50, null=True)),
                ('total_meta_fisica', models.IntegerField(blank=True, null=True, verbose_name='Total Meta Física')),
                ('meta_presupuestal', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('meta_fisica', models.PositiveIntegerField(default=0)),
                ('meta_programada', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('meta_anual', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('enero', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('febrero', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('marzo', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('abril', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('mayo', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('junio', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('julio', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('agosto', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('setiembre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('octubre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('noviembre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('diciembre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('enero_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('febrero_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('marzo_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('abril_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('mayo_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('junio_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('julio_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('agosto_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('setiembre_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('octubre_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('noviembre_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('diciembre_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('total_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('primer_semestre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('segundo_semestre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('primer_semestre_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('segundo_semestre_e', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('porcentaje', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'POI_META_FISICA',
            },
        ),
        migrations.CreateModel(
            name='ProgramacionMensual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(blank=True, choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=20, null=True)),
                ('meta_fisica', models.IntegerField()),
                ('meta_presupuestal', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('actividad_poi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discapacidad.actividadpoi')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramacionMensualMetaFinanciera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_programada', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('meta_anual', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('fuente_f', models.CharField(blank=True, max_length=100, null=True)),
                ('generico_gasto', models.CharField(blank=True, max_length=100, null=True)),
                ('enero', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('febrero', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('marzo', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('abril', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('mayo', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('junio', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('julio', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('agosto', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('setiembre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('octubre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('noviembre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('diciembre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('total', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('primer_semestre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('segundo_semestre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('porcentaje', models.CharField(blank=True, max_length=50, null=True)),
                ('actividad_poi', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='discapacidad.actividadpoi')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramacionMensualMetaFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(blank=True, choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=20, null=True)),
                ('meta_fisica', models.IntegerField()),
                ('meta_presupuestal', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('actividad_poi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discapacidad.actividadpoi')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramacionMetaFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(blank=True, choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio')], max_length=10, null=True)),
                ('meta_fisica', models.PositiveIntegerField(default=0)),
                ('meta_programada', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('meta_anual', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('enero', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('febrero', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('marzo', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('abril', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('mayo', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('junio', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('julio', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('agosto', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('setiembre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('octubre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('noviembre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('diciembre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('total', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('primer_semestre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('segundo_semestre', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('porcentaje', models.CharField(blank=True, max_length=50, null=True)),
                ('actividad_poi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discapacidad.actividadpoi')),
            ],
            options={
                'db_table': 'META_FISICA',
            },
        ),
    ]