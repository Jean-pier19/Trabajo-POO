
CREATE TABLE TipoEmpleado (
    id_tipo_emp INT PRIMARY KEY,
    identificacion VARCHAR(50) NOT NULL
);

CREATE TABLE Empleado (
    id_empleado INT PRIMARY KEY,
    id_tipo_emp INT,
    nombre VARCHAR(100),
    direccion VARCHAR(200),
    telefono VARCHAR(20),
    email VARCHAR(100),
    fecha_contrato DATE,
    salario DECIMAL(10, 2),
    FOREIGN KEY (id_tipo_emp) REFERENCES TipoEmpleado(id_tipo_emp)
);

CREATE TABLE Departamento (
    id_depto INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_empleado INT,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE Asignacion (
    id INT PRIMARY KEY,
    id_empleado INT,
    id_depto INT,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado),
    FOREIGN KEY (id_depto) REFERENCES Departamento(id_depto)
);

CREATE TABLE Proyecto (
    id_proyec INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE
);

CREATE TABLE ProyectoEmpleado (
    id_proyec_emp INT PRIMARY KEY,
    id_proyec INT,
    id_empleado INT,
    FOREIGN KEY (id_proyec) REFERENCES Proyecto(id_proyec),
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE RegistroTime (
    id INT PRIMARY KEY,
    id_proyec_emp INT,
    fecha DATE,
    horas INT,
    descripcion TEXT,
    FOREIGN KEY (id_proyec_emp) REFERENCES ProyectoEmpleado(id_proyec_emp)
);
