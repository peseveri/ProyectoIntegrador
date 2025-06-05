# Sistema de Analisis de Ventas

El objetivo de este proyecto es simular un flujo profesional donde se estructuran datos de ventas en una base de datos relacional y se modelan con POO.


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
├── Avance2/
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

Las pruebas unitarias están en Avance2/tests/test_patterns.py. Ejecútalas con:
    pytest Avance2/tests/

# Licencia
Este proyecto está bajo la Licencia MIT.

# Contacto
Para dudas o sugerencias, contacta al equipo de desarrollo en pedroseveri@gmail.com.