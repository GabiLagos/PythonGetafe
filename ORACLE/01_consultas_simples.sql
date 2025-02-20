-- COMNETARIOS

/*
COMENTARIOS DE VARIAS LINEAS
PODEMOS TENER TODAS LAS CONSULTAS QUE DESEEMOS
EN EL EDITOR, INDICAREMOS QUE CONSULTA QUEREMOS EJECUTAR
PARA EJCUTAR; CTL + ENTER (MAC)
NO DIFERNCIA MAYUSCULAS DE MINUSCULAS
LAS CONSULTAS FINALIZAN CON ;
*/

SELECT * FROM EMP where oficio='DIRECTOR';

/* 
OPERADORES RELACIONALES: AND OR 
TAMBIEN EXISTE NOT, PERO NO DEBEMOS USARLO PQ LA CONSULTA ES MUUUY INEFICIENTE!!!!
PERMITEN PREGUNTAR POR MAS DE UN FILTRO EN UNA MISMA CONSULTA
*/

Select emp_no, apellido, dept_no from emp where dept_no=10 or dept_no=20  order by emp_no;
SELECT * from emp where not oficio='VENDEDOR';
SELECT * from emp where  oficio <> 'VENDEDOR';

/* OTRO OPERADORES PARA FILTRAR; BETWEEN*/
SELECT * FROM EMP WHERE SALARIO BETWEEN 318000 AND 390000 ORDER BY SALARIO;

-- OPERADOR IN, BUSCA EN UN MISMO CAMPO (COLUMNA) MULTIPLES VALORES
select * from emp where dept_no in (10,20,30) order by 8,1;


-- OPERADOR BOT IN, BUSCA EN UN MISMO CAMPO (COLUMNA) MULTIPLES VALORES QUE NO ESTEN EN EL

select * from emp where dept_no not in (10,20) order by 8,1;

-- OPERADOR LIKE, SE UTILIZA PARA BUSCAR COINCIDENCIAS EN TEXTOS
-- REPRESENTA UN CARACTER CUALQUIERA "_"
select * from emp where apellido like 's%a';
select * from emp where apellido like '____';


/* CLAUSULA DISTINCT*/
select DISTINCT oficio from emp;

/* CAMPOS CALCULADOS
UN CAMPO CALCULADO ES UNA COLUMNA QUE NO EXISTE EN UNA TABLA PERO SE GENERA A PARTIR DE OTRA(S) COLUMNA(S)
LOS CAMPOS CALCULADOS NO SE PUEDEN FILTRAR COB WHERE PQ EN REALIDAD NO EXISTEN*/
SELECT APELLIDO, (SALARIO + COMISION) AS SALARIO_TOTAL FROM EMP;




/*  EJERCICIOS */

-- 01 Mostrar todos los datos de los empleados de nuestra tabla emp.
select * from emp;

-- 02 Mostrar el apellido, oficio, salario anual, con las dos extras para aquellos empleados con comisión mayor de 100000.
select apellido, oficio, salario*14 as salario_anual, comision from emp where comision>=100000;

-- 03 Idem del anterior, pero para aquellos empleados que su salario anual con extras supere las 750.000 ptas.
select apellido, oficio, salario*14 as salario_anual, comision from emp where (salario*12)>750000;

-- 04 Idem del anterior, pero para aquellos empleados que sumen entre salario anual con extras y comisión el 1.000.000. 
select apellido, oficio, salario*14 as salario_anual, comision   from emp where (salario*12+comision)>1000000;

-- 05 Mostrar todos los datos de empleados ordenados por departamento y dentro de este por oficio para tener una visión jerárquica.(order by)
select * from emp order by 8,3;
-- 06 Mostrar todos los enfermos nacidos antes del 1/1/70.
select * from enfermo where fecha_nac<'1/1/1970';

-- 07 Igual que el anterior, para los nacidos antes del 1/1/1970 ordenados por número de inscripción.
select * from enfermo where fecha_nac<'1/1/1970' order by 1;

-- 08 Listar todos los datos de la plantilla del hospital del turno de mañana
select * from plantilla where turno='M';

-- 09 Idem del turno de noche.
select * from plantilla where turno='N';

-- 10 Listar los doctores que su salario anual supere 3.000.000 ptas.
select  from doctor where ;

-- 11 Visualizar los empleados de la plantilla del turno de mañana que tengan un salario entre 2.000.000 y 2.250.000.
select * from plantilla;
Visualizar los empleados de la tabla emp que no se dieron de alta entre el 01/01/80 y el 12/12/82.
Mostrar los nombres de los departamentos situados en Madrid o en Barcelona.