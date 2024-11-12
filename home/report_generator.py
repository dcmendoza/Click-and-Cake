# account/report_generators.py
from abc import ABC, abstractmethod
import openpyxl
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data):
        pass

class ExcelReportGenerator(ReportGenerator):
    def generate_report(self, data):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Productos"
        
        ws.append(['Nombre', 'Precio', 'Tamaño', 'Sabor', 'Crema', 'Forma'])
        for product in data:
            ws.append([product.name, product.price, product.size, product.flavor, product.cream_flavor, product.shape])
        
        response = BytesIO()
        wb.save(response)
        response.seek(0)
        return response

class PDFReportGenerator(ReportGenerator):
    def generate_report(self, data):
        response = BytesIO()
        p = canvas.Canvas(response, pagesize=landscape)
        y_position = 750
        
        p.drawString(100, y_position, "Reporte de Productos")
        y_position -= 20
        p.drawString(100, y_position, "Nombre")
        p.drawString(200, y_position, "Precio")
        p.drawString(300, y_position, "Tamaño")
        p.drawString(400, y_position, "Sabor")
        p.drawString(500, y_position, "Crema")
        p.drawString(600, y_position, "Forma")
        y_position -= 20
        
        for product in data:
            p.drawString(100, y_position, product.name)
            p.drawString(200, y_position, str(product.price))
            p.drawString(300, y_position, product.size)
            p.drawString(400, y_position, product.flavor)
            p.drawString(500, y_position, product.cream_flavor)
            p.drawString(600, y_position, product.shape)
            y_position -= 20
        
        p.showPage()
        p.save()
        response.seek(0)
        return response
