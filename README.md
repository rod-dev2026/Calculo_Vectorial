# Cálculo Vectorial — Recursos Interactivos (ITTUX · TecNM)

Repositorio con aplicaciones de escritorio en **Python** y laboratorios web interactivos en **HTML5/JavaScript** diseñados para apoyar el aprendizaje de **Cálculo Vectorial (ACF-0904)** en el Instituto Tecnológico de Tuxtepec (TecNM)[cite: 1, 2, 3, 5].

El enfoque de estas herramientas es **visual, experimental y analítico**: permiten comprobar resultados, explorar geometría en 2D y 3D, manipular parámetros en tiempo real y conectar la formulación matemática con su interpretación geométrica y física[cite: 1, 2, 3, 4, 5].

## Contenido del repositorio

### Aplicaciones en Python
* **`UNIDAD 1 v0.3.py`** — Calculadora y graficador 3D (`Tkinter` + `NumPy` + `PyVista`) enfocado en la **Unidad 1 (Vectores en $\mathbb{R}^3$)**[cite: 3]. Incluye operaciones vectoriales, producto punto y ángulo, producto cruz, recta $r(t)$, triple producto escalar (con visualización del paralelepípedo) y ecuación del plano, con modo claro y oscuro[cite: 3].
* **`Unidad 1y2.py`** — Aplicación integral en `Tkinter` con pestañas para la **Unidad 1** (vectores y superficies en 3D con `PyVista`) y la **Unidad 2** (curvas paramétricas, derivadas paramétricas, longitud de arco y coordenadas polares graficadas con `Matplotlib`)[cite: 2].

### Laboratorios Web Interactivos (HTML5)
* **`index.html`** — Calculadora y visualizador multipestaña (**Unidades 1 a 5** del temario ACF-0904) con Canvas 2D/3D nativo, parser de expresiones matemáticas, ejemplos predefinidos por subtema y cambio de tema claro/oscuro[cite: 1].
* **`Funciones Lab PRO Responsive.html`** — Laboratorio interactivo 3D/2D con `Three.js` para curvas paramétricas, polares, cilíndricas, esféricas, superficies $z = f(x,y)$ y paramétricas, e implícitas 2D[cite: 4]. Permite animar un punto móvil $t$, visualizar tangente, velocidad, aceleración, triedro de Frenet, círculo osculador, sumas de Riemann, campos vectoriales, anotar puntos y exportar en PNG, SVG o JSON[cite: 4].
* **`Integrales Lab.html`** — Laboratorio de **Integración Múltiple** (dobles e iteradas en coordenadas rectangulares, dobles en polares, triples en rectangulares/cilíndricas/esféricas, integrales de línea escalares y vectoriales, divergencia y rotacional, y gradiente) con resolución paso a paso, cuadratura numérica, vista 3D/superior/corte y modo malla/sólido[cite: 5].

## Uso recomendado para estudiantes
1. **Para abrir los archivos `.html`**: haz doble clic sobre el archivo o ábrelo directamente en tu navegador web moderno (Chrome, Firefox, Edge, etc.)[cite: 1, 4, 5].
2. **Para ejecutar los scripts `.py`**: asegúrate de contar con Python 3 y las bibliotecas correspondientes (`numpy`, `pyvista`, `matplotlib`)[cite: 2, 3].
3. **Verificación y criterio propio**: usa estas herramientas para experimentar, formular hipótesis y validar tus procedimientos analíticos en libreta o en clase.

## Autoría y contexto académico
* **Autor / Diseñador:** Rod Compañ (Rodrigo Compañ Sarmiento)[cite: 1, 2, 3, 4, 5]
* **Institución:** Instituto Tecnológico de Tuxtepec (ITTUX) — Tecnológico Nacional de México (TecNM)[cite: 1, 2, 3, 5]
* **Asignatura:** Cálculo Vectorial (ACF-0904)[cite: 1, 5]
