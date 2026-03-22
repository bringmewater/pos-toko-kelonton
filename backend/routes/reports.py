from datetime import datetime

class SalesReport:
    def __init__(self):
        self.daily_sales = []
        self.monthly_sales = []
        self.top_products = {}

    def add_daily_sale(self, product, amount):
        self.daily_sales.append({'product': product, 'amount': amount, 'date': datetime.utcnow()})

    def add_monthly_sale(self, product, amount):
        self.monthly_sales.append({'product': product, 'amount': amount, 'date': datetime.utcnow()})

    def add_top_product(self, product, sales):
        self.top_products[product] = sales

    def generate_daily_sales_report(self):
        # Logic to generate daily sales report
        return self.daily_sales
    
    def generate_monthly_sales_report(self):
        # Logic to generate monthly sales report
        return self.monthly_sales
    
    def generate_top_products_report(self):
        # Logic to generate top products report
        return self.top_products
    
    def generate_sales_summary_report(self):
        # Logic to generate summary report
        return {
            'daily_sales': sum(sale['amount'] for sale in self.daily_sales),
            'monthly_sales': sum(sale['amount'] for sale in self.monthly_sales),
            'top_products': self.top_products
        }