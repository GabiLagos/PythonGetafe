/*
CONSULTAS DE AGRUPACION
Devuelven info acerca un determinado grupo.
Nunca devolveran elementos que corresponden a dicho grupo.
Se usan pata mostrar algun resumen de los datos

COUNT(*): cuenta el numero de regostros de un grupo. Tiene en cuenta los nuleos
COUNT)campo) cuenta el numero de registros de una colimna. NO tiene en cuenta los nulos
MAS(campo): devyelve el valor maximos de un campo
MIN(campo): igual, pero con el minmo
AVG(campo): devuelve la media de un conjunto
SUM(campo): devuelve la suma de un conjunto

Estas funciones se pueden comninar entre si.
Las columnas con funciones deben llevar siempre alias
*/


-- CONTAR EL NUMERO DE REGISTROS DE LA TABLA EMP
select count(*) as No_de_Registros from emp;

-- MOSTRAR EL NUMERO DE REGISTRO Y EL MAXIMO SALARIO DE EMP
select count (*) as No_de_Registros, max(salario) as Max_Salario from emp;

--MOSTRAR EL NUMERO DE PERSONAS POR CADA OFICIO EN CADA DEPARTAMENTO
select oficio, dept_no, count (*) as No_de_Empleados from emp group by oficio, dept_no order by 2;

--MOSTRAR EL NUMERO DE PERSONAS SON DIRECTOR O ANALISTA
select oficio, count (*) as No_de_Empleados from emp where oficio in ('DIRECTOR', 'ANALISTA') group by oficio;

select oficio, count (*) as No_de_Empleados from emp group by oficio having oficio in ('DIRECTOR', 'ANALISTA');

--MOSTRAR EL NUMERO DE PERSONAS SON DIRECTOR O ANALISTA DE LOS DEPARTAMENTOS 10 y 20
--MOSTRAR EL NUMERO DE PERSONAS POR CADA OFICIO DONDE EL NUMERO SEA MAS DE 2 PERSONAS
select oficio, dept_no, count (*) as No_de_Empleados from emp group by dept_no, oficio having count(*) >=2 ;


/*  EJERCICIOAS */

-- 01 Encontrar el salario medio de los analistas, mostrando el número de los empleados con oficio analista.
select oficio, avg (SALARIO) as Salario_Medio from emp 
group by oficio 
having oficio='ANALISTA';


select oficio, avg (SALARIO) as Salario_Medio from emp 
where oficio='ANALISTA'
group by oficio ;
	

-- 02 Encontrar el salario más alto, mas bajo y la diferencia entre ambos de todos los empleados con oficio EMPLEADO.

select  oficio, max(salario) as SALARIOMAXIMO
, min(salario) as SALARIOMINIMO
, max(salario) - min(salario) as DIFERENCIA 
from emp group by oficio having oficio = 'EMPLEADO';

-- 03 Visualizar los salarios mayores para cada oficio.
	
select oficio, max(salario) as SALARIOMAXIMO from emp group by oficio;

-- 04 Visualizar el número de personas que realizan cada oficio en cada departamento.

select dept_no, 
count(*) as PERSONAS, oficio
from emp group by dept_no, oficio
order by 1;

-- 05 Buscar aquellos departamentos con cuatro o más personas trabajando.
select dept_no
, count(*) as PERSONAS from emp 
group by dept_no having count(*) > 3;


-- 06 Mostrar el número de directores que existen por departamento.
select count(*) as NUMEROEMPLEADOS, dept_no 
from emp
where oficio = 'DIRECTOR'
group by dept_no;


-- 07 Visualizar el número de enfermeros, enfermeras e interinos que hay en la plantilla, ordenados por la función.
select funcion, count (funcion) as Num_Funcionarios from plantilla 
group by funcion;


-- 08 Visualizar departamentos, oficios y número de personas, para aquellos departamentos que tengan dos o más personas trabajando en el mismo oficio.

select dept_no 
,count(*) as PERSONAS, 
oficio from emp group by dept_no, oficio  
having count(*) > 1;

-- 09 Calcular el salario medio, Diferencia, Máximo y Mínimo de cada oficio. Indicando el oficio y el número de empleados de cada oficio.
select oficio, count(*) as EMPLEADOS
, min(salario) as SALARIOMAXIMO
, max(salario) as SALARIOMINIMO
, max(salario) - min(salario) as DIFERENCIA
, avg(salario) as MEDIA
 from emp group by  oficio;


-- 10 Calcular el valor medio de las camas que existen para cada nombre de sala. Indicar el nombre de cada sala y el número de cada una de ellas.
select nombre, sala_cod, round(avg(num_cama),2) as Media_de_camas_por_Sala from sala 
group by nombre, sala_cod;

-- 11 Calcular el salario medio de la plantilla de la sala 6, según la función que realizan. Indicar la función y el número de empleados.
select funcion, round(avg(salario),2), count(*) from plantilla 
where sala_cod=6
group by funcion;

-- 12 Averiguar los últimos empleados que se dieron de alta en la empresa en cada uno de los oficios, ordenados por la fecha.

select max(fecha_alt) AS FECHAMAXIMA, 
Oficio from emp
group by oficio
order by 1;

-- 13 Mostrar el número de hombres y el número de mujeres que hay entre los enfermos.
select sexo, count(sexo) as num_enfermos from enfermo 
group by sexo;

-- 14 Mostrar la suma total del salario que cobran los empleados de la plantilla para cada función y turno.
select turno, funcion, sum(salario) as Suma_Salario from plantilla 
group by turno, funcion;


-- 15 Calcular el número de salas que existen en cada hospital.
select count(*) as NUMEROSALAS
, hospital_cod from sala
group by hospital_cod;


-- 16 Mostrar el número de enfermeras que existan por cada sala.
select count(*) as PERSONAS
, sala_cod, funcion from plantilla
where funcion='ENFERMERA'
group by sala_cod, Funcion
order by 1;


