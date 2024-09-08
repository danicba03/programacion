SELECT * FROM Operario;

SELECT tipo, cantidad FROM Material;

SELECT nombre, edad FROM Operario WHERE edad > 30;

SELECT * FROM Material WHERE tipo LIKE 'C%';

SELECT * FROM Material ORDER BY cantidad DESC LIMIT 3;