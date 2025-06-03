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
│      └── test_models.py
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

Configurar el entorno virtual:
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar dependencias:
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

# Uso

Ejecutar el script principal:
    Los modelos en Avance1/src/models/ representan las entidades de la base de datos (categories, countries, cities, customers, employees, products, sales) y están mapeados utilizando SQLAlchemy para interactuar con la base de datos.
    Usa las clases definidas en Avance1/src/models/ para realizar operaciones como consultas, inserciones o análisis de datos con pandas.

# Ejecutar pruebas unitarias

Las pruebas unitarias están en Avance1/tests/test_models.py. Ejecútalas con:
    pytest Avance1/tests/

# Detalles del Script SQL

El archivo Avance1/sql/load_data.sql realiza las siguientes acciones:
    Crea la base de datos sales_company.
    Define las tablas relacionales: categories, countries, cities, customers, employees, products y sales.
    Carga los datos desde los archivos CSV ubicados en la carpeta data/ a las tablas correspondientes.

# Estructura de las Clases

Las clases en Avance1/src/models/ representan las entidades de la base de datos y están diseñadas con SQLAlchemy para facilitar el mapeo objeto-relacional. Cada clase (por ejemplo, Category, Country, Sale) corresponde a una tabla en la base de datos y permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

# Analisis de Datos

El proyecto utiliza pandas para manipular y analizar los datos cargados desde la base de datos. Puedes realizar consultas SQL y convertir los resultados en DataFrames para análisis avanzados, como cálculos de ventas totales, análisis por categoría o tendencias por fecha.

# Licencia
Este proyecto está bajo la Licencia MIT.

# Contacto
Para dudas o sugerencias, contacta al equipo de desarrollo en pedroseveri@gmail.com.