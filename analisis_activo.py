import yfinance as yf
import matplotlib.pyplot as plt
from fpdf import FPDF

class AnalisisActivo:
    def __init__(self, ticker, periodo="1mo"):
        self.ticker = ticker
        self.periodo = periodo
        self.datos = None
        self.precios = []

    def descargar_datos(self):
        activo = yf.Ticker(self.ticker)
        self.datos = activo.history(period=self.periodo)
        self.precios = self.datos["Close"].tolist()

    def promedio_movil(self, n):
        resultados = []
        for i in range(len(self.precios) - n + 1):
            ventana = self.precios[i:i + n]
            promedio = sum(ventana) / n
            resultados.append(promedio)
        return resultados

    def graficar(self, n, output="grafico.png"):
        pm = self.promedio_movil(n)
        plt.figure(figsize=(10, 5))
        plt.plot(self.precios, label="Precio cierre", marker="o", color="gray")
        plt.plot(range(n - 1, len(self.precios)), pm, label=f"Prom. móvil {n} días", color="blue")
        plt.title(f"Análisis de {self.ticker}")
        plt.xlabel("Días")
        plt.ylabel("Precio (USD)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(output)
        plt.close()

    def exportar_pdf(self, imagen="grafico.png", nombre_pdf="reporte.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"Reporte de {self.ticker}", ln=1, align="C")
        pdf.ln(10)
        pdf.image(imagen, x=10, y=30, w=190)
        pdf.output(nombre_pdf)
        print(f"PDF exportado como {nombre_pdf}")

analisis = AnalisisActivo("AAPL", periodo="1mo")  # Apple
analisis.descargar_datos()
analisis.graficar(n=5)  # promedio de 5 días
analisis.exportar_pdf()