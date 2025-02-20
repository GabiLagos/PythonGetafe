/*CONSULTAS DE ACCION
DML: Data Management Language

INSERT: inserta nuevos datos (filas o filas) en una tabla
utiliza la tabla como patron, es decir, los valores que pongamos 
serán los valores de la tabla en el orden que esten las columnas de la tabla
SINTAXIS:
insert into tabla values (valor1,valor2,valor3,...)
o 
insert intp tabla (columna1, columna2,...) values (valor1,valor2,...)


UPDATE: modifica uno o varios registros de una tabla, a la vez. 
Y en la misma consulta podemos indicar que sdeseamos mofdificar mas de una columna
SINTAXIS:
update tabla set columna1=valor1, columna2=valor2;

Esto modificará todos los registros de la columna, si se quiere un registro específico hay que incluir 
alguna otra condición mediante un where.


DELETE: elimina uno o varios registros de las tablas. Si la tabla no tiene 'where' elimina todos los registros de la tabla!!
SINTAXIS:
delete from table where condicion;
*/


insert into dept values (50,'PYTHON', 'GETAFE');

insert into dept (dept_no, dnombre) values (60, 'I+D');

-- Las subconsultas en DML son muy útiles, nos permiten recuperar datos de otras tablas o generar elementos dinámicos para las consultas
-- Por ejemplo: tenemos una nieva persona en la pantilla; Se apellida Lopez y su puesto de enfermera de tarde en el hospital 22
-- asignar el siguiente ID de empleado disponible al insertar el registro
select * from plantilla;
insert into plantilla (empleado_no, apellido, funcion, turno, hospital_cod) values ((select max(empleado_no)+1 from plantilla) , 'super-lópez', 'ENFERMERA', 'T', 22);
commit;


delete from plantilla where empleado_no>9901;  
-- Tambien se pueden user subconsultas en el delete
-- Por ejemplo, eliminar a las personas de la plantilla del Hospital El Carmen
delete from plantilla where (select hospital_cod from hospital where nombre='el carmen'); -- NOTA: no existe este hospital

rollback; -- deshace todo lo hecho ANTES de commit

 

--incremetar el salario de toda la plantilla
select * from plantilla;
update plantilla set salario= salario+1;
-- cambiar la funcion 'INTERINO' a 'INTERINA' y subie el salario en 1
update plantilla set funcion='INTERINA', salario=salario+1
where funcion='INTERINO';
--tambien se pueden usar subconsultas tanto en del set y/o en where
--igualar el salario de la plantilla de la sala 4 al salario de karplus
select salario from plantilla where apellido ='karplus w.';
update plantilla set salario=(select salario from plantilla where apellido ='karplus w.') where sala_cod=4;
--modificar a turno de mañana a todos los empleados de la sala de piquiatria
select sala_cod from sala where nombre='psiquiatria';
UPDATE plantilla set turno='M' where sala_cod=(select distinct sala_cod from sala where nombre='psiquiatria');

/*EJECICIOS*/
-- Insertar una nueva persona en plantilla: se apellida cabrales, en la sala 4, es enfermera, turno mañanas, en el hospital El Carmen
-- su ID será eñ maximo en la consulta.
-- Luego eliminar las personas que no tengan hospital

select * from hospital;
select max(empleado_no)+1 from plantilla;
insert into hospital (hospital_cod, nombre) values (50, 'el carmen');
insert into plantilla ( sala_cod, empleado_no, apellido, funcion, turno) 
values ( 4, (select max(empleado_no)+1 from plantilla), 'cabrales1', 'ENFERMERA', 'M');


DELETE FROM plantilla WHERE hospital_cod is null;
DELETE FROM plantilla WHERE salario is null;



