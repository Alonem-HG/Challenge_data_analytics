
CREATE OR REPLACE VIEW REGISTROS_POR_CATEGORIA AS
SELECT categoria, Count(categoria) as total
FROM info_cultural GROUP BY categoria; 


CREATE OR REPLACE VIEW REGISTROS_POR_FUENTE AS
SELECT fuente, COUNT(fuente) as total 
FROM info_cultural GROUP BY fuente;


CREATE OR REPLACE VIEW REGISTROS_POR_PROVINCIA_CATEGORIA AS
SELECT COUNT(*), provincia, categoria
from info_cultural
group by provincia, categoria
order by provincia, categoria;


