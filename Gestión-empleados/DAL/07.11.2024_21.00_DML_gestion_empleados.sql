
INSERT INTO tipoempleado (id_tipo_emp, identificacion)
VALUES
(1, 'ID001'),
(2, 'ID002'),
(3, 'ID003'),
(2, 'ID004'),
(1, 'ID005');

INSERT INTO empleado (id_empleado, id_tipo_emp, identificacion, nombre, direccion, telefono, email, fecha_contrato, salario)
VALUES
(1, 1, 'ID001', 'Juan Perez', 'Calle Falsa 123, Santiago', '987654321', 'juan.perez@example.com', '2023-01-15', 1000.00),
(2, 2, 'ID002', 'Ana Lopez', 'Avenida Siempre Viva 456, Santiago', '987654322', 'ana.lopez@example.com', '2022-12-10', 1500.00),
(3, 3, 'ID003', 'Luis Garcia', 'Callejón del Agua 789, Santiago', '987654323', 'luis.garcia@example.com', '2022-11-05', 1200.00),
(4, 1, 'ID004', 'Maria Fernandez', 'Camino Real 101, Santiago', '987654324', 'maria.fernandez@example.com', '2023-02-20', 2000.00),
(5, 2, 'ID005', 'Carlos Martinez', 'Plaza Mayor 202, Santiago', '987654325', 'carlos.martinez@example.com', '2023-03-11', 1800.00);
