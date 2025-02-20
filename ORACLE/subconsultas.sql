/*
SUBCONSULTAS
SON SONSULTAS EN LAS QUE NECESITAMOS EN RESULTADO DE OTRA CONSULTA PARA PODER 
EJECUTARLA.

sintaxis:
select * from primera_consulta
where dato = (consulta_anidada);

*/

-- MOSTRAR LOS DATOS DEL EMPLEADO QUE MAS COBRA DE LA EMPRESA
select * from emp;

select * from emp
where salario = (select max(salario) from emp);

/* PUEDE HABER VARIOS   ANIDAMIENTOS O MAS NIVELES DE ANIDAMIENTO (SUBCONSULTAS
DENTRO DE SUBCONSULTAS.
SI EL RESULTADO DE LA SUBCONSULTA ES MAS DE UN VALOR, LA CONSULTA GENERAL DARA 
UN ERROR(EXCEPCION).
 MOSTRAR TODOS LOS EMPLEADOS QUE TENGAN EL MISMO OFICIO QUE EL EMPLEADO 
DE APELLIDO 'SALA' Y QUE TENGAN MAS SALARIO DE EL EMPLEADO DE APELLIDO 'FORD' */

select * from emp;
select oficio from emp where apellido='sala';
select salario from emp where apellido='ford';
select oficio from emp where apellido='jimenez';

select * from emp 
where 
    oficio=(select oficio from emp where apellido='sala') 
    and salario > (select salario from emp where apellido='ford');
    
    
/* MOSTRAR TODOS LOS EMPLEADOS QUE TENGAN EL MISMO OFICIO QUE EL EMPLEADO 
DE APELLIDO 'SALA' Y EL MISMO OFICIO QUE JIMENEZ*/

select oficio from emp where apellido='sala' or apellido='jimenez'; -- <- SUBCONSULTA, devuelve mas de un valor

select * from emp 
where 
    oficio=(select oficio from emp where apellido='sala' or apellido='jimenez');  -- Esta consulta nos dará una excepcion
    
    
select * from emp 
where 
    oficio in (select oficio from emp where apellido ='sala' or apellido='jimenez') ;  -- Usamos IN para que la subconsulta funcione
    



/*EJERCICIOS*/

/*1. Mostrar el número de empleado, el apellido y la fecha de alta del 
empleado más antiguo de la empresa. */
select * from emp
order by fecha_alt;

select emp_no, apellido, fecha_alt from emp
where fecha_alt=(select min(fecha_alt) from emp);

/*2.Mostrar el número de empleado, el apellido y la fecha de alta del empleado
más moderno de la empresa. */

select emp_no, apellido, fecha_alt from emp
where fecha_alt=(select max(fecha_alt) from emp);

/*3.Visualizar el apellido y el salario de los empleados con el mismo oficio que Jiménez. */
select apellido, oficio, salario from emp 
where oficio=(select oficio from emp where apellido='jimenez');


/*4.Queremos saber el apellido, oficio, salario y número de departamento de los empleados 
con salario mayor que el mejor salario del departamento 30. */
select apellido, oficio, salario, dept_no from emp
where salario>(select max(salario) from emp where dept_no=30);

/*5. Mostrar el apellido, la función u oficio, sala o departamento de todos los empleados 
que trabajen en Empresa o Plantilla.*/
select * from plantilla;
select p.apellido, p.funcion as "funcion/oficio", s.nombre "sala/departamento" from plantilla p
join sala s
on p.sala_cod=s.sala_cod

union 

select e.apellido, e.oficio, d.dnombre from emp e
join dept d
on d.dept_no=e.dept_no;