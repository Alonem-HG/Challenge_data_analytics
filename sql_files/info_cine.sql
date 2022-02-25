
CREATE OR REPLACE VIEW CINE_INFO AS
SELECT provincia, 
SUM(pantallas) as num_pantallas, 
SUM(butacas) as num_butacas,
SUM(espacio_incaa) as num_espacio
FROM info_cine
GROUP BY provincia
ORDER BY provincia ASC;



