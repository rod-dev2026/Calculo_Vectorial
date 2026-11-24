# Cálculo Vectorial — Recursos Interactivos (ITTUX · TecNM)

Repositorio con aplicaciones de escritorio en **Python** y laboratorios web interactivos en **HTML5/JavaScript** creados para acompañar el curso de **Cálculo Vectorial (ACF-0904)** en el Instituto Tecnológico de Tuxtepec (TecNM).

El propósito de este material es fomentar la exploración visual, la experimentación y el razonamiento analítico: los estudiantes pueden probar ejemplos, modificar parámetros, observar el comportamiento geométrico en 2D y 3D y contrastar sus cálculos con la interpretación física y matemática.

## Archivos del repositorio

### Scripts y aplicaciones en Python
* **`UNIDAD 1 v0.3.py`** — Calculadora y graficador 3D (`Tkinter`, `NumPy` y `PyVista`) orientado a la **Unidad 1 (Vectores en $\mathbb{R}^3$)**. Soporta suma, resta, escalares, magnitud y unitario, distancia, producto punto y ángulo, producto cruz, recta $r(t)$, triple producto escalar (con paralelepípedo en 3D) y ecuación del plano, con modo claro y oscuro.
* **`Unidad 1y2.py`** — Aplicación en `Tkinter` dividida en pestañas para la **Unidad 1** (vectores y superficies 3D con `PyVista`) y la **Unidad 2** (curvas paramétricas, derivadas paramétricas, longitud de arco y coordenadas polares graficadas con `Matplotlib`).

### Laboratorios Web Interactivos (HTML5)
* **`index.html`** — Calculadora y visualizador general de las **Unidades 1 a 5** del temario ACF-0904 con Canvas 2D/3D nativo, evaluador de expresiones matemáticas, ejemplos por subtema y selector de tema claro/oscuro.
* **`Funciones Lab PRO Responsive.html`** — Laboratorio interactivo 2D/3D basado en `Three.js` para curvas paramétricas, polares, cilíndricas y esféricas, superficies $z = f(x,y)$ y paramétricas, e implícitas 2D. Incluye punto móvil $t$, vector posición, tangente, velocidad, aceleración, triedro de Frenet, círculo osculador, sumas de Riemann, campos vectoriales, anotación de puntos y exportación a PNG, SVG y JSON.
* **`Integrales Lab.html`** — Laboratorio de **Integración Múltiple** para integrales dobles e iteradas en coordenadas rectangulares, dobles en polares, triples en rectangulares/cilíndricas/esféricas, integrales de línea escalares y vectoriales, divergencia y rotacional, y gradiente. Ofrece desarrollo paso a paso, cuadratura numérica, vistas 3D/superior/corte y alternancia entre malla y sólido.

## Cómo utilizarlos
1. **Archivos `.html`**: ábrelos directamente en cualquier navegador web actualizado (no requieren instalación adicional).
2. **Archivos `.py`**: ejecútalos en un entorno de Python 3 con las dependencias correspondientes (`numpy`, `pyvista`, `matplotlib`).
3. **Criterio académico**: utiliza estas herramientas para visualizar, comprobar y comprender los conceptos; el planteamiento y la justificación analítica siguen siendo clave en tu formación.

## Créditos
* **Autor / Diseñador:** Rod Compañ (Rodrigo Compañ Sarmiento)
* **Institución:** Instituto Tecnológico de Tuxtepec (ITTUX) — Tecnológico Nacional de México (TecNM)
* **Asignatura:** Cálculo Vectorial (ACF-0904)
