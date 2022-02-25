CREATE TABLE public.info_cine (
    cod_localidad numeric NOT NULL,
    id_provincia numeric NOT NULL,
    id_departamento numeric NOT NULL,
    categoria text NOT NULL,
    provincia text,
    localidad text,
    nombre text,
    domicilio text,
    codigo_postal text,
    mail text,
    web text,
    fuente text,
    numero_telefono text,
    pantallas numeric,
    butacas numeric,
    espacio_incaa numeric,
    fecha_carga date
);

ALTER TABLE public.info_cine OWNER TO postgres;


CREATE TABLE public.info_cultural (
    cod_localidad numeric NOT NULL,
    id_provincia numeric NOT NULL,
    id_departamento numeric NOT NULL,
    categoria text NOT NULL,
    provincia text,
    localidad text,
    nombre text,
    domicilio text,
    codigo_postal text,
    mail text,
    web text,
    fuente text,
    numero_telefono text,
    fecha_carga date
);


ALTER TABLE public.info_cultural OWNER TO postgres;