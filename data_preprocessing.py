import pandas as pd
import datetime
import os
from loggin import logging_options

log = logging_options.setup_logger("data_preprocessing")

df_cine = pd.read_csv("cine/2022-02/cine-24-02-2022.csv")
df_museo = pd.read_csv("museo/2022-02/museo-24-02-2022.csv")
df_biblioteca = pd.read_csv("biblioteca_popular/2022-02/biblioteca_popular-24-02-2022.csv")

def clean_data():
    df_cine.rename(columns={'Cod_Loc': 'cod_localidad',
                            'IdProvincia': 'id_provincia',
                            'IdDepartamento': 'id_departamento',
                            'Observaciones': 'observaciones',
                            'Categoría': 'categoria',
                            'Provincia': 'provincia',
                            'Departamento': 'departamento',
                            'Localidad': 'localidad',
                            'Nombre': 'nombre',
                            'Dirección': 'domicilio',
                            'Piso': 'piso',
                            'CP': 'codigo_postal',
                            'Teléfono': 'numero_telefono',
                            'Mail': 'mail',
                            'Web': 'web',
                            'Fuente': 'fuente',
                            'Pantallas': 'pantallas',
                            'Butacas': 'butacas',
                            'espacio_INCAA': 'espacio_incaa'}, inplace=True)

    df_museo.rename(columns={'Cod_Loc': 'cod_localidad',
                            'IdProvincia': 'id_provincia',
                            'IdDepartamento': 'id_departamento',
                            'Observaciones': 'observaciones',
                            'categoria': 'nombre_espacio',
                            'subcategoria': 'categoria',
                            'direccion': 'domicilio',
                            'CP': 'codigo_postal',
                            'telefono': 'numero_telefono',
                            'Mail': 'mail',
                            'Web': 'web',
                            'Fuente': 'fuente'}, inplace=True)

    df_biblioteca.rename(columns={'Cod_Loc': 'cod_localidad',
                                'IdProvincia': 'id_provincia',
                                'IdDepartamento': 'id_departamento',
                                'Observacion': 'observacion',
                                'Categoría': 'categoria',
                                'Subcategoria': 'subcategoria',
                                'Provincia': 'provincia',
                                'Departamento': 'departamento',
                                'Localidad': 'localidad',
                                'Nombre': 'nombre',
                                'Domicilio': 'domicilio',
                                'CP': 'codigo_postal',
                                'Cod_tel': 'cod_tel',
                                'Teléfono': 'numero_telefono',
                                'Mail': 'mail',
                                'Web': 'web',
                                'Fuente': 'fuente'}, inplace=True)

    df_cine['espacio_incaa'].fillna(0, inplace=True)
    df_cine['espacio_incaa'] = df_cine['espacio_incaa'].replace(['si', 'SI'], [ 1, 1])
    df_cine['espacio_incaa'] = df_cine['espacio_incaa'].astype('int64')
    df_cine['pantallas'] = df_cine['pantallas'].astype('int64')
    df_cine['butacas'] = df_cine['butacas'].astype('int64')

    df_museo['categoria'] = df_museo['categoria'].fillna("Museos")

    df_cine_sql = df_cine.drop(['observaciones',
                                'departamento',
                                'piso',
                                'cod_area',
                                'Información adicional',
                                'Latitud',
                                'Longitud',
                                'TipoLatitudLongitud',
                                'tipo_gestion',
                                'año_actualizacion'], axis=1)

    df_museo.drop(['observaciones',
                'nombre_espacio',
                'cod_area',
                'Info_adicional',
                'Latitud',
                'Longitud',
                'TipoLatitudLongitud',
                'piso',
                'año_inauguracion',
                'jurisdiccion',
                'IDSInCA'], axis=1, inplace=True)

    df_biblioteca.drop(['observacion',
                        'subcategoria',
                        'departamento',
                        'Piso',
                        'cod_tel',
                        'Información adicional',
                        'Latitud',
                        'Longitud',
                        'TipoLatitudLongitud',
                        'Tipo_gestion',
                        'año_inicio',
                        'Año_actualizacion'], axis=1, inplace=True)


    # Error typing son lo mismo
    df_cine_sql.provincia = df_cine_sql.provincia.replace(
        ['Ciudad Autónoma de Buenos Aires'], 'Buenos Aires')

    df_cine.drop(['observaciones',
                'departamento',
                'piso',
                'cod_area',
                'Información adicional',
                'Latitud',
                'Longitud',
                'TipoLatitudLongitud',
                'tipo_gestion',
                'año_actualizacion',
                'pantallas',
                'butacas',
                'espacio_incaa'], axis=1, inplace=True)

    df_merge = pd.concat([df_cine, df_museo, df_biblioteca])

    df_merge.provincia = df_merge.provincia.replace(
        ['Neuquén', 'Neuquén '], ['Neuquén', 'Neuquén'])  # Error typing agregaron espacio
    df_merge.provincia = df_merge.provincia.replace(
        ['Santa Fe'], 'Santa Fé')  # Error typing el acento
    df_merge.provincia = df_merge.provincia.replace(
        ['Ciudad Autónoma de Buenos Aires'], 'Buenos Aires')  # Error typing variacion de nombre
    # Error typing usaron el nombre mas largo
    df_merge.provincia = df_merge.provincia.replace(
        ['Tierra del Fuego, Antártida e Islas del Atlántico Sur'], 'Tierra del Fuego')

    # Agregar nueva columna 'fecha_carga'
    def today_date():
        '''
        utils:
        get the datetime of today
        '''
        date = datetime.datetime.now().date()
        #date = datetime.datetime.now().strftime("%d-%m-%Y")
        date = pd.to_datetime(date)
        date = pd.to_datetime(date, format='%d-%m-%Y')
        return date

    df_merge['fecha_carga'] = today_date()
    df_cine_sql['fecha_carga'] = today_date()

    s = '\\'
    time_ym = datetime.datetime.now().strftime("%Y-%m")
    time_dmy = datetime.datetime.now().strftime("%d-%m-%Y")

    if not os.path.exists('data_complete' + s + time_ym + s):
        os.makedirs('data_complete' + s + time_ym + s, exist_ok=True)
        df_merge.to_csv('data_complete' + s + time_ym + s +
                        'info_completa.csv', index=False, encoding='utf-8')
        log.debug("Directory..." + "data_complete" + s + time_ym + s + "was created")

        df_cine_sql.to_csv('data_complete' + s + time_ym + s +
                        'info_cine.csv', index=False, encoding='utf-8')
        log.info("info_completa.csv, info_cine.csv were created")

    else:
        log.debug("Directory..." + "data_complete" + s + time_ym + s + "already exist")
        df_merge.to_csv('data_complete' + s + time_ym + s +
                        'info_completa.csv', index=False, encoding='utf-8')

        df_cine_sql.to_csv('data_complete' + s + time_ym + s +
                        'info_cine.csv', index=False, encoding='utf-8')
        log.info("info_completa.csv, info_cine.csv were created")

    log.debug("Preprocessing is complete")