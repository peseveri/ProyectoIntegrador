import datetime
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.category import Category
from src.models.country import Country
from src.models.city import City
from src.models.customer import Customer
from src.models.employee import Employee
from src.models.product import Product
from src.models.sale import Sale

def test_category_get_id_name():
    cat = Category(1, "Bebidas")
    assert cat.get_id_name() == (1, "Bebidas")

def test_country_is_code_valid():
    country = Country(1, "Argentina", "AR")
    assert country.is_code_valid() is True

def test_city_belongs_to_country():
    city = City(10, "Buenos Aires", "1000", 1)
    assert city.belongs_to_country(1) is True
    assert city.belongs_to_country(2) is False

def test_customer_full_name():
    customer = Customer(5, "Juan", "M", "Pérez", 3, "Calle Falsa 123")
    assert customer.full_name() == "Juan M. Pérez"

def test_employee_years_worked():
    hire_date = datetime.datetime(2020, 5, 1)
    emp = Employee(1, "Ana", "L", "Gómez", datetime.datetime(1990, 4, 1), "F", 1, hire_date)
    assert emp.years_worked(2025) == 5

def test_product_is_expensive():
    prod = Product(1, "Jugo", 150.0, 2, "Clase A", "12:00", "Sí", "No", 30)
    assert prod.is_expensive() is True
    assert prod.is_expensive(threshold=200) is False

def test_sale_final_price_per_unit():
    sale = Sale(1, 2, 3, 4, 2, 0.1, 100.0, datetime.datetime(2023, 5, 1), "TX123")
    assert sale.final_price_per_unit() == 50.0
