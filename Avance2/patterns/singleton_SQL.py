import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine.base import Engine
from typing import Optional
from dotenv import load_dotenv

class MySQLConnection:
    _instance: Optional["MySQLConnection"] = None
    _engine: Optional[Engine] = None
    _SessionLocal = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MySQLConnection, cls).__new__(cls)
            cls._instance._init_engine()
        return cls._instance

    def _init_engine(self):
        load_dotenv()

        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "3306")
        db = os.getenv("DB_NAME")

        if not all([user, password, host, port, db]):
            raise ValueError("Faltan variables de entorno para la conexión a la base de datos.")

        url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"
        self._engine = create_engine(url, pool_pre_ping=True)
        self._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

    def get_session(self) -> Session:
        return self._SessionLocal()

    def execute_query(self, sql_query: str) -> pd.DataFrame:
        """Ejecuta una consulta SQL simple y devuelve un DataFrame con los resultados."""
        with self.get_session() as session:
            result = session.execute(text(sql_query))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df

    def close_engine(self):
        """Cierra manualmente el engine para liberar recursos si es necesario."""
        if self._engine:
            self._engine.dispose()
            self._engine = None
            self._SessionLocal = None

            print("Finalizada la conexion a la base")
