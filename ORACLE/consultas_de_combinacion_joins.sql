/*CONSULTAS DE COMBINACION
Permiten mostrar datos de multiples tablas relacionadas entre si en un mismo resultado
Las tablas deben tener relacion entre si
Se realizan combinando tablas con multiples campos mostrados en panatalla

Sintaxis:
select tabla1.campo1, tabla1.campo2, tabla2.campo1, tabla2,campo2
from tabla1
inner join tabla2
on tabla1.camporelacion = tabla2.camporelacion

Ni importa en orden de las tabas.
*/

select * from emp E
inner join dept D
on E.dept_no=D.dept_no; -- aqui estoy viendo juntos todos los campos de las tablas emp y dept

-- MUESTRA EL NOMBRE DE LOS EMPLEADOS SU FUNCION, DEPARTAMENTO Y LOCALIDAD
select e.apellido as nombre, e.oficio as oficio, d.dnombre as departamento, d.loc as localidad from emp E
INNER join dept D
on E.dept_no=D.dept_no
order by 4; 

-- MUESTRA EL NOMBRE DE LOS EMPLEADOS SU FUNCION, DEPARTAMENTO Y LOCALIDAD QUE TRABAJAM EN SEVILLA
select e.apellido as nombre, e.oficio as oficio, d.dnombre as departamento, d.loc as localidad from emp E
inner join dept D
on E.dept_no=D.dept_no 
where d.loc='SEVILLA';

-- PODEMOS COMBINAR ESTA CONSULTAS CON FUNCIONES DE AGRUPACION
-- MUESTRA EL NUMERO DE PERSONAS POR CADA DEPARTAMENTO
select D.dnombre, count(*) as Num_Empleados from emp E
inner join dept D
on E.dept_no=D.dept_no
group by D.dnombre;


-- MOSTRAR EL APELLIDO, FUNCION Y NOMBRE DE HOSPITAL DE LAS PERSONAS DE LA PLANTILLA
select * from plantilla;
select * from hospital;

select P.apellido, P.funcion, H.nombre from plantilla P
inner join hospital H
on P.hospital_cod = H.hospital_cod
order by 3,2;

/*
DENTRO DE LAS CONSULTAS DE COMBINACION TENEMOS OTROS TIPOS DE CONSULTAS:
INNER JOIN: DATOS COMUNES ENTRE LAS DOS TABLAS
LEFT JOIN: LOS DATOS COMUNES Y LOS DATOS DE LA TABLAS DE LA IZQ, la tabla antes del join
RIGHT JOIN: LOS MISMO PERO CON LA TABLA DE LA DERECHA, la tabla despues del join
FULL JOIN: RECUPERA TODO, COMBINENE O NO
CROSS JOIN: PRODUCTO CARTESIANO
*/

select * from dept;
SELECT * FROM emp;

SELECT * from dept D
full join emp E       -- aqui jugamos cambiando left, right, inner o full
on d.dept_no=e.dept_no;

SELECT * from dept D
cross join emp E ;      -- cross join NO lleva on

/*EJERCICIOS*/

-- 01 Mostrar apellido, salario y especialidad de los doctores de La Paz
SELECT * FROM  hospital;
select * from doctor;
select * from plantilla;
select d.apellido, d.salario, d.especialidad, h.direccion from doctor d
join hospital h
on d.hospital_cod=h.hospital_cod
where h.nombre='la paz';

-- 02 mostrar cuantos empleados hay en cada departamento mostrando el nombre del departamento
select * from dept;
select * from emp;

select d.dnombre, d.loc, count (emp_no) 
from emp e
right join dept d
on d.dept_no=e.dept_no
group by d.dnombre, d.loc
order by 3;

/* LAS CUNSULTAS SE PUEDEN HACER CON MULTIPLES TABLAS, O SEA, MAS DE DOS TABLAS RELACIONADAS.
LO QUE IMPLICA QUE TENGO QUE HACER VARIOS JOINS, UNA POR CADA PAR DE TABLAS RELACIONADAS

SINTAXIS:
select tabla1.campo, tabla1.campo2
, tabla.campo1, tabla2.campo2
,tabla3.campo1, tabla3.campo2
from tabla1
inner join tabla2
on tabla1.camporelacion=tabla2.camporalacion
inner join tabla3
on tabla2.camporelacion=tabla3.camporelacion;
*/

select * from sala;
select * from hospital;
select * from plantilla order by 3;

select distinct p.apellido, p.funcion, s.nombre as Sala, h.nombre as Hospital from plantilla p
inner join hospital h
on p.hospital_cod=h.hospital_cod
inner join sala s
on s.sala_cod=p.sala_cod
order by 1;


-- otra manera...
select  p.apellido, p.funcion, s.nombre as Sala, h.nombre as Hospital from plantilla p
inner join hospital h
on p.hospital_cod=h.hospital_cod

inner join sala s
on s.sala_cod=p.sala_cod
and s.hospital_cod=h.hospital_cod -- notese el AND. Esto se debe a que plantilla y sala tambien se relacionan a traves de sala_cod

order by 1;



-- EJERCICIOS

--1. Seleccionar el apellido, oficio, salario, numero de departamento y su nombre de todos 
--los empleados cuyo salario sea mayor de 300000

select * from emp;
select * from dept;

select e.apellido, e.oficio, e.salario, e.dept_no, d.dnombre from emp e
join dept d
on d.dept_no=e.dept_no
where e.salario>300000
order by 3;

/* 2. Mostrar todos los nombres de Hospital con sus nombres de salas correspondientes. */
select * from hospital;
select * from sala;

select h.nombre as hospital, s.nombre as sala from hospital h
join sala s
on s.hospital_cod=h.hospital_cod
order by 1,2;

/*3. Calcular cuántos trabajadores de la empresa hay en cada ciudad.*/
select * from emp;
select * from dept;

select D.loc, count(e.emp_no) as Num_Empleados from emp E
right join dept D
on E.dept_no=D.dept_no
group by D.loc
order by 2;


/*4. Visualizar cuantas personas realizan cada oficio en cada departamento 
mostrando el nombre del departamento.*/

select * from emp;
select * from dept;

select d.dnombre, e.oficio, count(e.emp_no) from emp e
join dept d
on E.dept_no=D.dept_no
group by d.dnombre,e.oficio 
order by 1, 2;

/*5. Contar cuantas salas hay en cada hospital, mostrando el nombre de las 
salas y el nombre del hospital. */

select * from sala;
select * from hospital;

select h.nombre as hospital, s.nombre as sala, count(s.sala_cod) from sala s
join hospital h
on h.hospital_cod=s.hospital_cod
group by h.nombre, s.nombre;

/*6. Queremos saber cuántos trabajadores se dieron de alta entre el año 
1997 y 1998 y en qué departamento.
*/
 
select * from emp;
select * from dept;

select d.dnombre, count(e.emp_no) from emp e
join dept d
on d.dept_no=e.dept_no
group by d.dnombre;

/*7. Buscar aquellas ciudades con cuatro o más personas trabajando.*/
select * from emp;
select * from dept;

select D.loc, count(e.emp_no) as Num_Empleados from emp E
right join dept D
on E.dept_no=D.dept_no
having count(e.emp_no)>=4
group by D.loc
order by 2;

/*8. Calcular la media salarial por ciudad.  Mostrar solamente la media 
para Madrid y Elche.*/
select * from emp;
select * from dept;

select D.loc, round(avg(e.salario),2) as edia_salario from emp E
right join dept D
on E.dept_no=D.dept_no
having d.loc in ('MADRID', 'ELCHE')
group by D.loc
order by 2;


/*9.Mostrar los doctores junto con el nombre de hospital en el que ejercen, 
la dirección y el teléfono del mismo. */
select * from hospital;
select * from doctor;

select d.apellido as doctor, h.nombre as hospital, h.direccion, h.telefono from doctor d
join hospital h
on h.hospital_cod=d.hospital_cod
order by 2;

/*10. Mostrar los nombres de los hospitales junto con el mejor salario 
de los empleados de la plantilla de cada hospital.*/
select * from hospital;
select * from plantilla;

select h.nombre as hospital,  max(p.salario) from hospital h
join plantilla p
on p.hospital_cod=h.hospital_cod
group by h.nombre
order by 1;

/*11. Visualizar el Apellido, función y turno de los empleados de la plantilla 
junto con el nombre de la sala y el nombre del hospital con el teléfono.*/
select * from hospital;
select * from plantilla;
select * from sala;
select p.apellido, p.funcion, p.turno, h.nombre as hospital, s.nombre as sala  from plantilla p
join sala s
on s.hospital_cod=p.hospital_cod
and s.sala_cod=p.sala_cod
join hospital h
on h.hospital_cod=p.hospital_cod
order by 3,1;


/*12.Visualizar el máximo salario, mínimo salario de los Directores dependiendo de la ciudad
en la que trabajen. Indicar el número total de directores por ciudad.*/
select * from emp;

select d.loc, max(e.salario), min(e.salario), count(e.oficio) from emp e
join dept d
on d.dept_no=e.dept_no
where e.oficio='DIRECTOR'
group by d.loc
order by 1;

/*13. Averiguar la combinación de que salas podría haber por cada uno de los hospitales. */
select h.nombre as hospital, s.nombre as sala from sala s
cross join hospital h