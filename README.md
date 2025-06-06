# Sistema de Analisis de Ventas

El objetivo de este proyecto es simular un flujo profesional donde se estructuran datos de ventas en una base de datos relacional y se modelan con POO.

# ------------------------------------------------------------- AVANCE 1 -----------------------------------------------------------------------------------------------------

# Estructura del Proyecto

ProyectoIntegrador/
├── Avance1/
│   ├── data/
│   │   ├── categories.csv
│   │   ├── sales.csv
│   │   ├── cities.csv
│   │   ├── countries.csv
│   │   ├── customers.csv
│   │   ├── employees.csv
│   │   └── products.csv
│   ├── sql/
│   │   └── load_data.sql
│   ├── src/
│   │   └── models/
│   │       ├── category.py
│   │       ├── country.py
│   │       ├── city.py
│   │       ├── customer.py
│   │       ├── employee.py
│   │       ├── product.py
│   │       └── sale.py
│   ├── tests/
│   │   └── test_models.py
├── Avance2y3/
│   ├── patterns/
│   │   ├── builder_SQL.py
│   │   ├── singleton_SQL.py
│   │   └── strategy_SQL.py
│   ├── tests/
│   │   └── test_patterns.py
│   └── main.ipynb
├── .env
├── .gitignore
├── README.md
└── requirements.txt


# Requisitos

Python: Versión 3.8 o superior.
MySQL: Versión 8.0 o superior.
Dependencias de Python (listadas en requirements.txt):
    pandas==2.2.3: Para manipulación y análisis de datos.
    mysql-connector-python==9.3.0: Para conectar Python con MySQL.
    SQLAlchemy==2.0.40: Para mapeo objeto-relacional (ORM).
    python-dotenv==1.1.0: Para cargar variables de entorno desde un archivo .env.
    pytest==8.3.5: Para ejecutar pruebas unitarias.

# Configuración del Entorno

Clonar el repositorio:
    git clone <URL_DEL_REPOSITORIO>
    cd HenryProyectoIntegrador

# Configurar el entorno virtual:
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias:
    pip install -r requirements.txt

# Configurar la base de datos:

Asegúrate de tener MySQL 8.0 o superior instalado y en ejecución.
Copia los archivos CSV de la carpeta data/ a la ruta especificada en secure_file_priv de MySQL (por ejemplo, C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/). Para verificar esta ruta, ejecuta:
    SHOW VARIABLES LIKE 'secure_file_priv';

Ejecuta el script SQL sql/load_data.sql para crear la base de datos y cargar los datos o abrir el load_data.sql desde el workbench y correr las queries.

# Configurar variables de entorno

DB_HOST=localhost
DB_USER=<tu_usuario>
DB_PASSWORD=<tu_contraseña>
DB_NAME=sales_company


# Ejecutar pruebas unitarias del avance 1

Las pruebas unitarias están en Avance1/tests/test_models.py. Ejecútalas con:
    pytest Avance1/tests/

# Detalles del Script SQL

El archivo Avance1/sql/load_data.sql realiza las siguientes acciones:
    Crea la base de datos sales_company.
    Define las tablas relacionales: categories, countries, cities, customers, employees, products y sales.
    Carga los datos desde los archivos CSV ubicados en la carpeta data/ a las tablas correspondientes.

# Estructura de las Clases

Las clases en Avance1/src/models/ representan las entidades de la base de datos y tienen metodos relevantes para el negocio.

# Analisis de Datos

El proyecto utiliza pandas para manipular y analizar los datos cargados desde la base de datos. Puedes realizar consultas SQL y convertir los resultados en DataFrames para análisis avanzados.

# ------------------------------------------------------------- AVANCE 2 -----------------------------------------------------------------------------------------------------
# Patrones de Diseño Aplicados

En la segunda etapa del proyecto (Avance2) se implementaron patrones de diseño para mejorar la modularidad, mantenimiento y escalabilidad del sistema, enfocándose en la separación de responsabilidades y la reutilización del código.

# Singleton - MySQLConnection
    Descripción: Este patrón asegura que la conexión a la base de datos MySQL sea única en toda la aplicación, evitando múltiples conexiones simultáneas que puedan saturar recursos o generar inconsistencias.

    Beneficios:

    Control centralizado de la conexión a la base de datos.

    Mejora en la gestión de recursos y desempeño.

    Facilita cambios futuros en la configuración de la conexión en un único lugar.

# Builder - QueryBuilder
    Descripción: Permite construir consultas SQL complejas de forma dinámica y legible mediante métodos encadenados, facilitando la composición modular de cláusulas SQL.

    Beneficios:

    Claridad en la construcción de consultas, evitando errores en concatenaciones manuales.

    Flexibilidad para crear consultas personalizadas sin duplicar código.

    Facilita la extensión y mantenimiento del código relacionado a consultas SQL.

# Strategy - KPIBaseStrategy y KPIContext
    Descripción: Define una familia de algoritmos (cálculos de KPIs), encapsulándolos en clases independientes que pueden ser intercambiadas en tiempo de ejecución según la   necesidad.
    
    Beneficios:
    
    Modularidad en la implementación de diferentes KPIs, permitiendo agregar nuevos sin modificar la lógica existente.
    
    Facilita pruebas unitarias específicas para cada KPI.
    
    Mejora la escalabilidad y adaptabilidad del sistema frente a nuevos requerimientos analíticos.

# Pruebas Unitarias
    Se incluyó un conjunto de pruebas para verificar la correcta implementación y funcionamiento de los patrones y la integración con la base de datos:

    Singleton: Valida que la conexión a la base de datos sea efectivamente única.

    Builder: Verifica la estructura de las consultas SQL generadas dinámicamente.

    Strategy: Comprueba el cálculo correcto de KPIs como ventas totales, ventas por categoría y conteo de clientes.

    Estas pruebas aseguran la robustez y calidad del código, facilitando futuros desarrollos y mantenimiento.

# Ejecutar pruebas unitarias del avance 2

Las pruebas unitarias están en Avance2y3/tests/test_patterns.py. Ejecútalas con:
    pytest Avance2y3/tests/

# ------------------------------------------------------------- AVANCE 3 -----------------------------------------------------------------------------------------------------
# Optimización del Rendimiento con Índices

Se han creado índices estratégicos para acelerar las consultas y mejorar el rendimiento general de la base de datos. Los índices elegidos se basan en el patrón de uso y las relaciones entre tablas:

idx_sales_salespersonid en sales (SalesPersonID):
    Justificación: La columna SalesPersonID es un campo clave utilizado para unir la tabla sales con la tabla employees. Indexarla mejora drásticamente la velocidad de las consultas que buscan ventas por vendedor y optimiza el rendimiento de los JOINs en esta columna.
idx_sales_customerid en sales (CustomerId):
    Justificación: Similar a SalesPersonID, CustomerId es un campo clave que conecta sales con customers. Indexarla acelera las búsquedas de ventas por cliente y mejora la eficiencia de los JOINs relacionados.
La creación de índices se realiza desde Python utilizando el método execute_ddl de la clase MySQLConnection, lo que permite automatizar y versionar la gestión del esquema de la base de datos.

# Análisis de Datos con CTEs y Funciones de Ventana
Se han utilizado Common Table Expressions (CTEs) y Funciones de Ventana en SQL para realizar análisis de datos avanzados directamente en la base de datos:

CTE para ventas_por_producto:

    Propósito: Calcula el total de ventas por cada producto y permite filtrar productos que hayan tenido más de un cierto número de ventas (ej. más de 100).
    Justificación: Las CTEs mejoran la legibilidad y modularidad de consultas complejas. Permiten descomponer una consulta grande en pasos lógicos más pequeños y con nombre, lo que facilita su comprensión y mantenimiento. Es ideal para análisis por fases como este.

Función de Ventana para acumulado_cliente:

    Propósito: Para cada venta, muestra el total acumulado de ventas (cantidad) por cliente, ordenado cronológicamente.
    Justificación: Las funciones de ventana (SUM(...) OVER (PARTITION BY ... ORDER BY ...)) son herramientas SQL poderosas para realizar cálculos analíticos complejos sobre un conjunto de filas relacionadas. Permiten calcular totales acumulados, promedios móviles o clasificaciones sin necesidad de subconsultas correlacionadas o auto-uniones, lo que mejora la eficiencia y legibilidad del código SQL para análisis temporal y por grupo.

# Mejora de la Analítica con Funciones y Vistas en la Base de Datos

Para potenciar la capacidad de análisis y la reutilización de la lógica de negocio, se han implementado las siguientes estructuras directamente en la base de datos:

Vista detailed_sales_report:

    Propósito: Esta vista consolida la información de ventas, productos, categorías, clientes y empleados en una única "tabla virtual".
    Justificación: Simplifica drásticamente las consultas complejas. En lugar de escribir múltiples JOINs cada vez que se necesita un informe detallado de ventas, basta con consultar esta vista. Esto no solo mejora la legibilidad de las consultas, sino que también facilita un análisis de ventas enriquecido (por categoría, ubicación del cliente, vendedor, etc.) al tener todos los datos relevantes pre-unidos.
    Implementación: La vista se crea y se consulta directamente desde Python, lo que facilita su despliegue y uso programático.

Función CALCULATE_SALE_TOTAL_PRICE:

    Propósito: Esta función calcula el precio total de una línea de venta, aplicando un descuento a un precio unitario y una cantidad dada.
    Justificación:
    Reusabilidad: Permite reutilizar la lógica de cálculo del precio total en cualquier consulta SQL, procedimiento almacenado o aplicación, garantizando una consistencia en el cálculo del precio con descuento en todo el sistema.
    Modularidad: Encapsula una pieza de lógica de negocio compleja en un componente manejable.
    Claridad de Consultas: Mantiene las consultas SQL más limpias al delegar los cálculos a la función.
    Implementación: La función se crea y se llama desde Python, demostrando la capacidad de la aplicación para interactuar con la lógica de negocio a nivel de base de datos.


Este enfoque integral, combinando un diseño de esquema robusto, una gestión de conexiones eficiente y la implementación estratégica de índices, vistas, funciones y capacidades analíticas avanzadas en SQL, sienta las bases para una base de datos de ventas de alto rendimiento y fácil mantenimiento.

# Licencia
Este proyecto está bajo la Licencia MIT.

# Contacto
Para dudas o sugerencias, contacta al equipo de desarrollo en pedroseveri@gmail.com.