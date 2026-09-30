# Calculadora Interactiva de Cálculo Vectorial - Unidades 1 y 2 (TecNM)

Aplicación de escritorio desarrollada en Python diseñada para resolver, analizar y visualizar interactivamente los conceptos fundamentales de la **Unidad 1 ("Vectores en el espacio")** y la **Unidad 2 ("Curvas planas, ecuaciones paramétricas y coordenadas polares")** de la asignatura de **Cálculo Vectorial** (Clave: ACF-0904) del Tecnológico Nacional de México (TecNM).

---
## 🖼️ Vista Previa de la Aplicación

<p align="center">
  <img src="screenshoot.png" alt="Calculadora de Cálculo Vectorial - TecNM Tuxtepec" width="100%"/>
</p>

## 🚀 Características Principales

- **Interfaz Gráfica Adaptativa:** Selector dinámico de modo oscuro y modo claro mediante un botón de alternancia, organizado mediante una estructura de pestañas para la gestión modular de unidades.
- **Entrada Dinámica:** Configuración flexible de vectores en $\mathbb{R}^3$, puntos espaciales, funciones paramétricas $x(t), y(t)$, funciones polares $r(\theta)$ e intervalos escalares ($a, b, k, t$).
- **Motor Analítico Robusto:** Operaciones algebraicas exactas, de alta velocidad y cálculo diferencial impulsadas por **NumPy**.
- **Visualización Interactiva Avanzada:** 
  - Renderizado gráfico tridimensional en tiempo real utilizando **PyVista** (ejes coordenados, rejillas adaptativas, vectores, mallas y superficies transparentes para la Unidad 1).
  - Trazado gráfico bidimensional dinámico con **Matplotlib** para el análisis analítico de curvas paramétricas y sistemas polares (Unidad 2).
- **Consola de Resultados Integrada:** Historial detallado con barra de desplazamiento para consultar los valores analíticos devueltos.

---

## 📐 Operaciones Soportadas (Temario TecNM)

### Módulo Unidad 1: Vectores en el Espacio
| Operación / Concepto | Descripción Geométrica y Analítica |
| :--- | :--- |
| **Graficación de Vectores** | Representación espacial desde el origen con cálculo de magnitud, vector unitario y ángulos/cosenos directores ($\alpha, \beta, \gamma$). |
| **Suma y Resta Vectorial** | Visualización geométrica de la ley del triángulo y paralelogramo para operaciones binarias. |
| **Multiplicación por Escalar** | Ilustración del escalamiento, compresión e inversión de dirección de un vector en el espacio. |
| **Magnitud y Vector Unitario** | Cálculo de la norma de una entidad espacial y normalización de su dirección. |
| **Distancia entre Puntos** | Trazado de segmentos tubulares y esferas delimitadoras entre dos posiciones espaciales ($P_1 \rightarrow P_2$). |
| **Producto Punto y Ángulo** | Cálculo del producto escalar, ángulo analítico (radianes y grados) y representación de la proyección vectorial. |
| **Producto Cruz** | Generación del vector ortogonal resultante en $\mathbb{R}^3$ y su magnitud asociada. |
| **Ecuación de la Recta** | Modelado paramétrico de líneas rectas en el espacio a partir de un punto inicial y un vector director. |
| **Triple Producto Escalar** | Cálculo del volumen escalar y renderizado volumétrico transparente del paralelepípedo formado por tres vectores. |
| **Ecuación Vectorial del Plano** | Determinación de puntos base, vectores directores, vector normal ($n = u \times v$), ecuación general ($Ax + By + Cz = D$) y superficie mallada en 3D. |

### Módulo Unidad 2: Curvas Planas, Ecuaciones Paramétricas y Coordenadas Polares
| Operación / Concepto | Descripción Analítica y Gráfica |
| :--- | :--- |
| **Curvas Paramétricas (2.1)** | Representación y trazado de trayectorias en el plano $x(t)$ y $y(t)$ sobre un intervalo cerrado $[a, b]$[cite: 2]. |
| **Derivada y Concavidad (2.2)** | Cálculo analítico de la primera ($\frac{dy}{dx}$) y segunda derivada ($\frac{d^2y}{dx^2}$) para determinar pendientes y concavidad[cite: 2]. |
| **Rectas Tangentes y Normales (2.3)** | Determinación y representación gráfica superpuesta de la recta tangente en un punto específico ($t_0$)[cite: 2]. |
| **Longitud de Arco y Área (2.4)** | Evaluación numérica de la longitud de trayectoria y el área encerrada mediante integración discreta[cite: 2]. |
| **Coordenadas Polares (2.5)** | Conversión, análisis de puntos notables y graficación de funciones polares $r(\theta)$[cite: 2]. |
| **Cálculo Integral en Polares (2.6)** | Determinación de áreas de regiones delimitadas por curvas polares con sombreado dinámico de sectores circulares[cite: 2]. |

---

## 💻 Requisitos del Sistema

- **Python** 3.8 o superior.
- Librerías principales:
  - `numpy`
  - `pyvista`
  - `matplotlib`
  - `tkinter` (incluida por defecto en la mayoría de instalaciones de Python en Linux/Windows).

---

## 🛠️ Instalación y Ejecución

Clona el repositorio e instala las dependencias necesarias ejecutando los siguientes comandos en tu terminal:

```bash
# Clonar el repositorio
git clone [https://github.com/rod-dev2026/Vectorial-U1.git](https://github.com/rod-dev2026/Vectorial-U1.git)
cd Vectorial-U1

# Instalar dependencias requeridas
pip install numpy pyvista matplotlib

# Ejecutar la aplicación
python main.py
