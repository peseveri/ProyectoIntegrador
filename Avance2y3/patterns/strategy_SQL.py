from abc import ABC, abstractmethod

class KPIBaseStrategy(ABC):
    def __init__(self, db_connection):
        self.db = db_connection

    @abstractmethod
    def get_kpi(self):
        pass


class TotalSalesKPI(KPIBaseStrategy):
    def get_kpi(self):
        query = "SELECT SUM(TotalPrice) AS total_sales FROM sales"
        df = self.db.execute_query(query)
        return df["total_sales"].iloc[0] if not df.empty else 0


class SalesByCategoryKPI(KPIBaseStrategy):
    def get_kpi(self):
        query = """
        SELECT c.CategoryName, COUNT(*) AS total_sales
        FROM sales s
        JOIN products p ON s.ProductID = p.ProductID
        JOIN categories c ON p.CategoryID = c.CategoryID
        GROUP BY c.CategoryName
        ORDER BY total_sales DESC;
        """
        return self.db.execute_query(query)


class CustomersCountKPI(KPIBaseStrategy):
    def get_kpi(self):
        query = "SELECT COUNT(*) AS total_customers FROM customers"
        df = self.db.execute_query(query)
        return df["total_customers"].iloc[0] if not df.empty else 0


class KPIContext:
    def __init__(self, strategy: KPIBaseStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: KPIBaseStrategy):
        self._strategy = strategy

    def get_kpi(self):
        return self._strategy.get_kpi()
