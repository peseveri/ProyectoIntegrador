import sys
import os
from decimal import Decimal
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from patterns.singleton_SQL import MySQLConnection
from patterns.builder_SQL import QueryBuilder
from patterns.strategy_SQL import KPIContext, TotalSalesKPI, CustomersCountKPI, SalesByCategoryKPI


def test_singleton_connection():
    conn1 = MySQLConnection()
    conn2 = MySQLConnection()
    assert conn1 is conn2, "La conexión no es singleton"
    print("✔ test_singleton_connection passed")

def test_builder_query_structure():
    builder = QueryBuilder()
    query = (builder.select("c.CategoryName", "COUNT(s.TotalPrice) AS total_sales")
                   .from_table("sales s")
                   .join("JOIN products p ON s.ProductID = p.ProductID")
                   .join("JOIN categories c ON p.CategoryID = c.CategoryID")
                   .group_by("c.CategoryName")
                   .order_by("total_sales DESC")
                   .limit(3)
                   .build())
    
    assert "FROM sales s" in query
    assert "JOIN products p" in query
    assert "GROUP BY c.CategoryName" in query
    assert "ORDER BY total_sales DESC" in query
    assert "LIMIT 3" in query
    print("✔ test_builder_query_structure passed")

def test_strategy_total_sales_kpi():
    conn = MySQLConnection()
    context = KPIContext(TotalSalesKPI(conn))
    total_sales = context.get_kpi()

    assert isinstance(total_sales, (int, float, Decimal)), "Debe ser un número"
    assert total_sales >= 0, "Total de ventas no puede ser negativo"
    print("✔ test_strategy_total_sales_kpi passed")

def test_strategy_sales_by_category_kpi():
    conn = MySQLConnection()
    context = KPIContext(SalesByCategoryKPI(conn))
    df = context.get_kpi()

    assert not df.empty, "El KPI de ventas por categoría no devolvió resultados"
    assert "CategoryName" in df.columns
    assert "total_sales" in df.columns
    print("✔ test_strategy_sales_by_category_kpi passed")

def test_strategy_customers_count_kpi():
    conn = MySQLConnection()
    context = KPIContext(CustomersCountKPI(conn))
    count = context.get_kpi()

    assert isinstance(count, (int, float, np.integer)), "Debe ser un número"
    assert count >= 0, "El conteo de clientes no puede ser negativo"
    print("✔ test_strategy_customers_count_kpi passed")


def run_all_tests():
    test_singleton_connection()
    test_builder_query_structure()
    test_strategy_total_sales_kpi()
    test_strategy_sales_by_category_kpi()
    test_strategy_customers_count_kpi()
    print("✅ Todas las pruebas pasaron correctamente.")
