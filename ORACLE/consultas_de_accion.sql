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
update tabla set columna1=valor1, columna2=valor2 where;

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

/*EJERCICIOS*/
-- Insertar una nueva persona en plantilla: se apellida cabrales, en la sala 4, es enfermera, turno mañanas, en el hospital El Carmen
-- su ID será el maximo en la consulta.
-- Luego eliminar las personas que no tengan hospital

select * from hospital;
select max(empleado_no)+1 from plantilla;
insert into hospital (hospital_cod, nombre) values (50, 'el carmen');
insert into plantilla ( sala_cod, empleado_no, apellido, funcion, turno) 
values ( 4, (select max(empleado_no)+1 from plantilla), 'cabrales1', 'ENFERMERA', 'M');


DELETE FROM plantilla WHERE hospital_cod is null;
DELETE FROM plantilla WHERE salario is null;


/* 01. Dar de alta con fecha actual al empleado José Escriche Barrera como programador perteneciente al departamento de producción. 
Tendrá un salario base de 70000 pts/mes y no cobrará comisión. */
select * from emp;
select * from dept;

insert into emp (fecha_alt, apellido, oficio, dept_no, salario, comision, emp_no) 
values (sysdate, 'escriche barrera', 'PROGRAMADOR', (select dept_no from dept where dnombre='PRODUCCIÓN'), 70000, 0,(select max(emp_no)+1 from emp) );

-- 02. Se quiere dar de alta un departamento de informática situado en Fuenlabrada (Madrid).
select * from dept;
insert into dept values(70,'INFORMATICA', 'FUENLABRADA');

/* 03. El departamento de ventas, por motivos peseteros, se traslada a Teruel, realizar dicha modificación.
04. En el departamento anterior (ventas), se dan de alta dos empleados: Julián Romeral y Luis Alonso.  
Su salario base es el menor que cobre un empleado, y cobrarán una comisión del 15% de dicho salario.*/
select * from emp;
select * from dept;
update dept set loc='TERUEL' where dnombre='VENTAS';

insert into emp(fecha_alt, apellido, dept_no, salario, comision, emp_no) 
values(sysdate, 'romeral',(select dept_no from dept where dnombre='VENTAS') , (select min(salario) from emp), 0,(select max(emp_no)+1 from emp));

insert into emp (fecha_alt, apellido, dept_no, salario, comision, emp_no)
values(sysdate, 'alonso',(select dept_no from dept where dnombre='VENTAS') , (select min(salario) from emp), 0,(select max(emp_no)+1 from emp)); 

-- 05. Modificar la comisión de los empleados de la empresa, de forma que todos tengan un incremento del 10% del salario.
update emp set comision= comision + (salario*0.1);

-- 06. Incrementar un 5% el salario de los interinos de la plantilla que trabajen en el turno de noche.
select * from plantilla;
update plantilla set salario = salario*1.05 where funcion='INTERINA'; 

/*07 Incrementar en 5000 Pts. el salario de los empleados del departamento de ventas y del presidente, 
tomando en cuenta los que se dieron de alta antes que el presidente de la empresa.*/
select * from emp order by 5 asc;

update emp set salario =salario+5000 
where oficio='PRESIDENTE' or (dept_no=(select dept_no from dept where dnombre='VENTAS') and fecha_alt < (select fecha_alt from emp where oficio='PRESIDENTE'));

rollback;

/*08. El empleado Sanchez ha pasado por la derecha a un compañero.  Debe cobrar de comisión 12.000 ptas más que el empleado Arroyo 
y su sueldo se ha incrementado un 10% respecto a su compañero.*/
select * from emp where apellido in ('sanchez', 'arroyo');

update emp set 
comision =(select comision from emp where apellido='arroyo')+12000, 
salario= (select salario from emp where apellido='arroyo')*1.1
where apellido='sanchez';

/*09. Se tienen que desplazar cien camas del Hospital SAN CARLOS para un Hospital de Venezuela. 
Actualizar el número de camas del Hospital SAN CARLOS.*/
select * from hospital;
update hospital set num_cama=num_cama - 100 where nombre='san carlos';

/*10. Subir el salario y la comisión en 100000 pesetas y veinticinco mil pesetas 
respectivamente a los empleados que se dieron de alta en este año.*/
select * from emp;
update emp set salario=salario+100000, comision=comision+25000 where fecha_alt >= '01/01/25';

/*11. Ha llegado un nuevo doctor a la Paz.  Su apellido es House y su especialidad 
es Diagnostico.   Introducir el siguiente número de doctor disponible.*/
select * from doctor;
insert into doctor (doctor_no, apellido, especialidad, hospital_cod) 
values((select max(doctor_no)+1 from doctor),'House', 'Diagnostico', (select hospital_cod from hospital where nombre='la paz'));


-- 12. Borrar todos los empleados dados de alta entre las fechas 01/01/80 y 31/12/82.
select * from emp;
DELETE FROM emp WHERE fecha_alt between '01/01/80' and '31/12/94';

/* Modificar el salario de los empleados trabajen en la paz y estén destinados a Psiquiatría.  
Subirles el sueldo 20000 Ptas. más que al señor Amigo R.*/
select apellido, especialidad from doctor;
select * from plantilla;
select * from sala;

Insertar un empleado con valores null (por ejemplo la comisión o el oficio), y después borrarlo buscando como valor dicho valor null creado.

Borrar los empleados cuyo nombre de departamento sea producción.

Borrar todos los registros de la tabla Emp sin delete.

Volver a ejecutar los SCRIPTS de BBDD para dejar la base de datos intacta para el siguiente módulo.*/



