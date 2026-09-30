#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 2026
@author: Rod Compañ & Asistente
"""

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import pyvista as pv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Contexto matemático seguro para la Unidad 2
ALLOWED_GLOBALS = {
    "sin": np.sin, "cos": np.cos, "tan": np.tan,
    "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan,
    "sinh": np.sinh, "cosh": np.cosh, "tanh": np.tanh,
    "exp": np.exp, "log": np.log, "log10": np.log10,
    "sqrt": np.sqrt, "abs": np.abs, "pi": np.pi, "e": np.e,
    "floor": np.floor, "min": np.min, "max": np.max
}

def evaluar_expr(expr_str, t_val):
    try:
        expr_limpia = expr_str.replace("^", "**")
        contexto = ALLOWED_GLOBALS.copy()
        contexto["t"] = t_val
        contexto["theta"] = t_val
        resultado = eval(expr_limpia, {"__builtins__": {}}, contexto)
        return float(resultado)
    except Exception as e:
        raise ValueError(f"Error al evaluar la expresión '{expr_str}': {e}")

class CalculoVectorialMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Integral de Cálculo Vectorial - TecNM Tuxtepec")
        self.root.geometry("950x850+300+30")
        
        self.dark_mode = True
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Contenedor de Pestañas Principal
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Marcos de las pestañas
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text=" Unidad 1: Vectores en R3 (PyVista) ")
        self.notebook.add(self.tab2, text=" Unidad 2: Curvas y Polares (Matplotlib) ")

        # Aplicar tema y construir ambas unidades
        self.apply_theme()
        
        self.init_unidad1_widgets()
        self.init_unidad2_widgets()
        
        self.actualizar_grafica_u2()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()
        self.actualizar_grafica_u2()

    def apply_theme(self):
        if self.dark_mode:
            self.bg_main = "#1e1e1e"
            self.bg_frame = "#2d2d2d"
            self.fg_light = "#ffffff"
            self.accent_blue = "#007acc"
            self.accent_hover = "#005999"
            self.text_bg = "#252526"
            self.text_fg = "#d4d4d4"
            self.label_fg = "#66b2ff"
            self.pv_bg = "#111111"
            self.pv_grid = "#444444"
            self.mpl_bg = "#1e1e1e"
            self.mpl_fg = "#ffffff"
            self.mpl_grid = "#444444"
            self.theme_btn_text = "☀️ Modo Claro"
        else:
            self.bg_main = "#f0f2f5"
            self.bg_frame = "#e4e7eb"
            self.fg_light = "#111111"
            self.accent_blue = "#0066cc"
            self.accent_hover = "#004080"
            self.text_bg = "#ffffff"
            self.text_fg = "#000000"
            self.label_fg = "#004080"
            self.pv_bg = "#ffffff"
            self.pv_grid = "#cccccc"
            self.mpl_bg = "#ffffff"
            self.mpl_fg = "#111111"
            self.mpl_grid = "#cccccc"
            self.theme_btn_text = "🌙 Modo Oscuro"

        self.root.configure(background=self.bg_main)
        if hasattr(self, "theme_btn_1"):
            self.theme_btn_1.config(text=self.theme_btn_text)
        if hasattr(self, "theme_btn_2"):
            self.theme_btn_2.config(text=self.theme_btn_text)

        self.style.configure(".", background=self.bg_main, foreground=self.fg_light, fieldbackground=self.text_bg)
        self.style.configure("TLabel", background=self.bg_main, foreground=self.fg_light)
        self.style.configure("TLabelframe", background=self.bg_frame, foreground=self.label_fg)
        self.style.configure("TLabelframe.Label", background=self.bg_frame, foreground=self.label_fg, font=("Arial", 10, "bold"))
        self.style.configure("TRadiobutton", background=self.bg_frame, foreground=self.fg_light, focuscolor=self.bg_frame)
        self.style.map("TRadiobutton", background=[("active", self.bg_frame)], foreground=[("active", self.label_fg)])
        
        self.style.configure("TButton", background=self.accent_blue, foreground="#ffffff", borderwidth=1, focusthickness=3, focuscolor=self.accent_hover)
        self.style.map("TButton", background=[("active", self.accent_hover), ("pressed", "#00264d")])
        
        self.style.configure("TCombobox", fieldbackground=self.text_bg, foreground=self.fg_light, selectbackground=self.accent_blue, selectforeground="#ffffff")

        if hasattr(self, "text_output_1"):
            self.text_output_1.configure(background=self.text_bg, foreground=self.text_fg, insertbackground=self.fg_light)
        if hasattr(self, "text_output_2"):
            self.text_output_2.configure(background=self.text_bg, foreground=self.text_fg, insertbackground=self.fg_light)

    # ========================== UNIDAD 1 ==========================
    def init_unidad1_widgets(self):
        top_bar = ttk.Frame(self.tab1)
        top_bar.pack(fill="x", padx=10, pady=5)
        self.theme_btn_1 = ttk.Button(top_bar, text=self.theme_btn_text, command=self.toggle_theme)
        self.theme_btn_1.pack(side="right", padx=5)

        input_frame = ttk.LabelFrame(self.tab1, text=" Componentes de Vectores y Puntos ")
        input_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(input_frame, text="Vector a / P1 (x1, y1, z1):").grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.entry_a = ttk.Entry(input_frame, width=30)
        self.entry_a.insert(0, "1, 2, 3")
        self.entry_a.grid(row=0, column=1, padx=5, pady=4)

        ttk.Label(input_frame, text="Vector b / P2 (x2, y2, z2):").grid(row=1, column=0, sticky="w", padx=5, pady=4)
        self.entry_b = ttk.Entry(input_frame, width=30)
        self.entry_b.insert(0, "4, 1, 2")
        self.entry_b.grid(row=1, column=1, padx=5, pady=4)

        ttk.Label(input_frame, text="Vector c / P3 (x3, y3, z3):").grid(row=2, column=0, sticky="w", padx=5, pady=4)
        self.entry_c = ttk.Entry(input_frame, width=30)
        self.entry_c.insert(0, "2, 3, 5")
        self.entry_c.grid(row=2, column=1, padx=5, pady=4)

        ttk.Label(input_frame, text="Escalar (k) / Parámetro (t):").grid(row=3, column=0, sticky="w", padx=5, pady=4)
        self.entry_scalar = ttk.Entry(input_frame, width=30)
        self.entry_scalar.insert(0, "2")
        self.entry_scalar.grid(row=3, column=1, padx=5, pady=4)

        sel_frame = ttk.LabelFrame(self.tab1, text=" Selector de Operandos ")
        sel_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(sel_frame, text="Operando principal (Op1):").grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.combo_op1 = ttk.Combobox(sel_frame, values=["a", "b", "c"], width=8, state="readonly")
        self.combo_op1.set("a")
        self.combo_op1.grid(row=0, column=1, padx=5, pady=4, sticky="w")

        ttk.Label(sel_frame, text="Operando secundario (Op2):").grid(row=0, column=2, sticky="w", padx=15, pady=4)
        self.combo_op2 = ttk.Combobox(sel_frame, values=["a", "b", "c"], width=8, state="readonly")
        self.combo_op2.set("b")
        self.combo_op2.grid(row=0, column=3, padx=5, pady=4, sticky="w")

        op_frame = ttk.LabelFrame(self.tab1, text=" Operaciones de la Unidad 1 ")
        op_frame.pack(fill="x", padx=10, pady=5)

        self.operation_var_1 = tk.StringVar(value="Triple Producto Escalar")
        operations = [
            "Graficar Vector Individual (Op1)", "Suma (Op1 + Op2)", "Resta (Op1 - Op2)", 
            "Multiplicacion por Escalar (k*Op1)", "Magnitud y Vector Unitario (Op1)", 
            "Distancia entre Puntos (Op1->Op2)", "Producto Punto y Angulo", "Producto Cruz (Op1 x Op2)", 
            "Ecuacion de la Recta r(t)", "Triple Producto Escalar", "Ecuacion Vectorial del Plano"
        ]

        for i, op in enumerate(operations):
            rb = ttk.Radiobutton(op_frame, text=op, variable=self.operation_var_1, value=op)
            rb.grid(row=i//2, column=i%2, sticky="w", padx=10, pady=2)

        btn_frame = ttk.Frame(self.tab1)
        btn_frame.pack(fill="x", padx=10, pady=6)

        calc_btn = ttk.Button(btn_frame, text="Calcular Analítico", command=self.calcular_u1)
        calc_btn.pack(side="left", expand=True, fill="x", padx=5)

        plot_btn = ttk.Button(btn_frame, text="Graficar en 3D (PyVista)", command=self.graficar_pyvista)
        plot_btn.pack(side="right", expand=True, fill="x", padx=5)

        result_frame = ttk.LabelFrame(self.tab1, text=" Resultados Analíticos ")
        result_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.text_output_1 = tk.Text(result_frame, height=5, width=70)
        self.text_output_1.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=self.text_output_1.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_output_1.configure(yscrollcommand=scrollbar.set)

    def parse_vector(self, text):
        if not text.strip():
            return None
        try:
            return np.array([float(x.strip()) for x in text.split(",")])
        except Exception:
            return None

    def obtener_vector_por_nombre(self, nombre):
        if nombre == "a": return self.parse_vector(self.entry_a.get())
        elif nombre == "b": return self.parse_vector(self.entry_b.get())
        elif nombre == "c": return self.parse_vector(self.entry_c.get())
        return None

    def calcular_u1(self):
        op = self.operation_var_1.get()
        name1, name2 = self.combo_op1.get(), self.combo_op2.get()
        v1, v2, v3 = self.obtener_vector_por_nombre(name1), self.obtener_vector_por_nombre(name2), self.obtener_vector_por_nombre("c")

        if v1 is None:
            messagebox.showerror("Error", f"El vector Operando 1 ('{name1}') es inválido.")
            return

        try:
            k = float(self.entry_scalar.get())
        except ValueError:
            k = 1.0

        output = ""
        if op == "Graficar Vector Individual (Op1)":
            mag = np.linalg.norm(v1)
            unit = v1 / mag if mag != 0 else np.zeros_like(v1)
            output = f"Vector [{name1}]: {v1}\nMagnitud: {mag:.4f}\nUnitario: {unit}"
        elif op == "Suma (Op1 + Op2)": output = f"Suma = {v1 + v2}"
        elif op == "Resta (Op1 - Op2)": output = f"Resta = {v1 - v2}"
        elif op == "Multiplicacion por Escalar (k*Op1)": output = f"Escalar = {k * v1}"
        elif op == "Magnitud y Vector Unitario (Op1)":
            mag = np.linalg.norm(v1)
            output = f"Magnitud: {mag:.4f}\nUnitario: {v1/mag}"
        elif op == "Distancia entre Puntos (Op1->Op2)": output = f"Distancia: {np.linalg.norm(v2 - v1):.4f}"
        elif op == "Producto Punto y Angulo":
            dot = np.dot(v1, v2)
            deg = np.degrees(np.arccos(np.clip(dot/(np.linalg.norm(v1)*np.linalg.norm(v2)), -1, 1)))
            output = f"Punto: {dot}\nÁngulo: {deg:.2f}°"
        elif op == "Producto Cruz (Op1 x Op2)":
            cross = np.cross(v1, v2)
            output = f"Cruz: {cross}\nMagnitud: {np.linalg.norm(cross):.4f}"
        elif op == "Ecuacion de la Recta r(t)": output = f"r({k}) = {v1 + k * v2}"
        elif op == "Triple Producto Escalar":
            tp = np.dot(self.obtener_vector_por_nombre("a"), np.cross(self.obtener_vector_por_nombre("b"), self.obtener_vector_por_nombre("c")))
            output = f"Triple Producto Escalar: {tp:.4f}"
        elif op == "Ecuacion Vectorial del Plano":
            n = np.cross(v2, v3)
            output = f"Normal: {n}\nPlano: {n[0]}x + {n[1]}y + {n[2]}z = {np.dot(n, v1):.4f}"

        self.text_output_1.delete("1.0", tk.END)
        self.text_output_1.insert(tk.END, output)

    def add_vector_fixed_thickness(self, plotter, start, direction, color, label=""):
        vec = np.array(direction, dtype=float)
        mag = np.linalg.norm(vec)
        if mag < 1e-6: return
        arrow = pv.Arrow(start=(0, 0, 0), direction=(0, 0, 1), shaft_radius=0.03, tip_radius=0.08, tip_length=0.25, scale=1.0)
        arrow.scale([1.0, 1.0, mag], inplace=True)
        z_axis, target_dir = np.array([0.0, 0.0, 1.0]), vec / mag
        dot = np.dot(z_axis, target_dir)
        if abs(dot + 1.0) < 1e-6: arrow.rotate_x(180, inplace=True)
        elif abs(dot - 1.0) > 1e-6:
            axis = np.cross(z_axis, target_dir)
            arrow.rotate_vector(axis / np.linalg.norm(axis), np.degrees(np.arccos(np.clip(dot, -1.0, 1.0))), inplace=True)
        arrow.translate(start, inplace=True)
        plotter.add_mesh(arrow, color=color, label=label if label else None)

    def graficar_pyvista(self):
        try:
            name1, name2 = self.combo_op1.get(), self.combo_op2.get()
            v1, v2 = self.obtener_vector_por_nombre(name1), self.obtener_vector_por_nombre(name2)
            a_full, b_full, c_full = self.obtener_vector_por_nombre("a"), self.obtener_vector_por_nombre("b"), self.obtener_vector_por_nombre("c")
            v1_3 = np.array([v1[0], v1[1], v1[2] if len(v1) > 2 else 0.0])
            v2_3 = np.array([v2[0], v2[1], v2[2] if len(v2) > 2 else 0.0]) if v2 is not None else None

            plotter = pv.Plotter()
            plotter.set_background(self.pv_bg)
            plotter.add_axes()
            plotter.show_grid(color=self.pv_grid)
            origin = np.array([0.0, 0.0, 0.0])
            op = self.operation_var_1.get()

            if op == "Graficar Vector Individual (Op1)":
                self.add_vector_fixed_thickness(plotter, origin, v1_3, "#0066cc", f"Vector {name1}")
            elif "Suma" in op and v2_3 is not None:
                self.add_vector_fixed_thickness(plotter, origin, v1_3, "#0066cc", f"Vector {name1}")
                self.add_vector_fixed_thickness(plotter, v1_3, v2_3, "#28a745", f"Vector {name2}")
                self.add_vector_fixed_thickness(plotter, origin, v1_3 + v2_3, "#dc3545", "Suma")
            elif op == "Triple Producto Escalar" and a_full is not None and b_full is not None and c_full is not None:
                a3, b3, c3 = np.array([a_full[0], a_full[1], a_full[2]]), np.array([b_full[0], b_full[1], b_full[2]]), np.array([c_full[0], c_full[1], c_full[2]])
                self.add_vector_fixed_thickness(plotter, origin, a3, "#0066cc", "a")
                self.add_vector_fixed_thickness(plotter, origin, b3, "#28a745", "b")
                self.add_vector_fixed_thickness(plotter, origin, c3, "#fd7e14", "c")
                r, s, t = np.linspace(0, 1, 5), np.linspace(0, 1, 5), np.linspace(0, 1, 5)
                R, S, T = np.meshgrid(r, s, t, indexing='ij')
                sgrid = pv.StructuredGrid(R*a3[0] + S*b3[0] + T*c3[0], R*a3[1] + S*b3[1] + T*c3[1], R*a3[2] + S*b3[2] + T*c3[2])
                plotter.add_mesh(sgrid.extract_surface(), color="#6f42c1", opacity=0.3, label="Paralelepípedo")
            else:
                self.add_vector_fixed_thickness(plotter, origin, v1_3, "#0066cc", f"Vector {name1}")

            plotter.add_legend()
            plotter.show()
        except Exception as e:
            messagebox.showerror("Error PyVista", str(e))

    # ========================== UNIDAD 2 ==========================
    def init_unidad2_widgets(self):
        main_container = ttk.Frame(self.tab2)
        main_container.pack(fill="both", expand=True, padx=10, pady=5)

        left_panel = ttk.Frame(main_container)
        left_panel.pack(side="left", fill="y", padx=5, pady=5)

        top_bar = ttk.Frame(left_panel)
        top_bar.pack(fill="x", pady=2)
        self.theme_btn_2 = ttk.Button(top_bar, text=self.theme_btn_text, command=self.toggle_theme)
        self.theme_btn_2.pack(side="right", padx=2)

        input_frame = ttk.LabelFrame(left_panel, text=" Parámetros (Unidad 2) ")
        input_frame.pack(fill="x", pady=4)

        ttk.Label(input_frame, text="Función x(t) o r(θ):").grid(row=0, column=0, sticky="w", padx=4, pady=2)
        self.entry_fx = ttk.Entry(input_frame, width=22)
        self.entry_fx.insert(0, "2*cos(t)")
        self.entry_fx.grid(row=0, column=1, padx=4, pady=2)

        ttk.Label(input_frame, text="Función y(t) [Paramétrica]:").grid(row=1, column=0, sticky="w", padx=4, pady=2)
        self.entry_fy = ttk.Entry(input_frame, width=22)
        self.entry_fy.insert(0, "2*sin(t)")
        self.entry_fy.grid(row=1, column=1, padx=4, pady=2)

        ttk.Label(input_frame, text="Límite Inferior (a / θ_min):").grid(row=2, column=0, sticky="w", padx=4, pady=2)
        self.entry_ta = ttk.Entry(input_frame, width=22)
        self.entry_ta.insert(0, "0")
        self.entry_ta.grid(row=2, column=1, padx=4, pady=2)

        ttk.Label(input_frame, text="Límite Superior (b / θ_max):").grid(row=3, column=0, sticky="w", padx=4, pady=2)
        self.entry_tb = ttk.Entry(input_frame, width=22)
        self.entry_tb.insert(0, "2*pi")
        self.entry_tb.grid(row=3, column=1, padx=4, pady=2)

        ttk.Label(input_frame, text="Valor t₀ / θ₀ a evaluar:").grid(row=4, column=0, sticky="w", padx=4, pady=2)
        self.entry_t0 = ttk.Entry(input_frame, width=22)
        self.entry_t0.insert(0, "pi/4")
        self.entry_t0.grid(row=4, column=1, padx=4, pady=2)

        op_frame = ttk.LabelFrame(left_panel, text=" Subtemas Unidad 2 ")
        op_frame.pack(fill="x", pady=4)

        self.operation_var_2 = tk.StringVar(value="2.1 Gráfica de Curvas Paramétricas")
        operations_u2 = [
            "2.1 Gráfica de Curvas Paramétricas", "2.2 Derivada de una función paramétrica", 
            "2.3 Rectas Tangentes y Normales", "2.4 Área y Longitud de Arco", 
            "2.5 Coordenadas Polares y Gráficas", "2.6 Cálculo en Coordenadas Polares"
        ]

        for op in operations_u2:
            ttk.Radiobutton(op_frame, text=op, variable=self.operation_var_2, value=op).pack(anchor="w", padx=6, pady=1)

        btn_frame = ttk.Frame(left_panel)
        btn_frame.pack(fill="x", pady=4)
        ttk.Button(btn_frame, text="Calcular", command=self.calcular_u2).pack(side="left", expand=True, fill="x", padx=2)
        ttk.Button(btn_frame, text="Graficar 2D", command=self.actualizar_grafica_u2).pack(side="right", expand=True, fill="x", padx=2)

        result_frame = ttk.LabelFrame(left_panel, text=" Resultados ")
        result_frame.pack(fill="both", expand=True, pady=4)

        self.text_output_2 = tk.Text(result_frame, height=5, width=38)
        self.text_output_2.pack(side="left", fill="both", expand=True, padx=2, pady=2)

        right_panel = ttk.LabelFrame(main_container, text=" Visualización Matplotlib 2D ")
        right_panel.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_panel)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def calcular_u2(self):
        op = self.operation_var_2.get()
        fx_s, fy_s = self.entry_fx.get(), self.entry_fy.get()
        try:
            a, b, t0 = evaluar_expr(self.entry_ta.get(), 0), evaluar_expr(self.entry_tb.get(), 0), evaluar_expr(self.entry_t0.get(), 0)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        output = ""
        if "2.1" in op:
            output = f"Punto en t₀: P({evaluar_expr(fx_s, t0):.4f}, {evaluar_expr(fy_s, t0):.4f})"
        elif "2.2" in op:
            h = 1e-5
            xp, yp = (evaluar_expr(fx_s, t0+h)-evaluar_expr(fx_s, t0-h))/(2*h), (evaluar_expr(fy_s, t0+h)-evaluar_expr(fy_s, t0-h))/(2*h)
            output = f"dy/dx = {yp/xp if xp!=0 else 'Indefinido'}"
        elif "2.4" in op:
            t_vals = np.linspace(a, b, 1000)
            dt = t_vals[1] - t_vals[0]
            l = sum(np.sqrt(((evaluar_expr(fx_s, t+1e-5)-evaluar_expr(fx_s, t-1e-5))/2e-5)**2 + ((evaluar_expr(fy_s, t+1e-5)-evaluar_expr(fy_s, t-1e-5))/2e-5)**2)*dt for t in t_vals[:-1])
            output = f"Longitud de arco = {l:.4f}"
        else:
            output = f"Cálculo ejecutado para {op}"

        self.text_output_2.delete("1.0", tk.END)
        self.text_output_2.insert(tk.END, output)

    def actualizar_grafica_u2(self):
        try:
            op = self.operation_var_2.get()
            fx_s, fy_s = self.entry_fx.get(), self.entry_fy.get()
            a, b, t0 = evaluar_expr(self.entry_ta.get(), 0), evaluar_expr(self.entry_tb.get(), 0), evaluar_expr(self.entry_t0.get(), 0)

            self.fig.clear()
            self.fig.patch.set_facecolor(self.mpl_bg)
            ax = self.fig.add_subplot(111)
            ax.set_facecolor(self.mpl_bg)

            if "Polares" in op:
                th = np.linspace(a, b, 1000)
                r = np.array([evaluar_expr(fx_s, t) for t in th])
                ax.plot(r * np.cos(th), r * np.sin(th), color="#007acc", linewidth=2)
            else:
                tv = np.linspace(a, b, 1000)
                ax.plot([evaluar_expr(fx_s, t) for t in tv], [evaluar_expr(fy_s, t) for t in tv], color="#007acc", linewidth=2)

            ax.grid(True, color=self.mpl_grid, linestyle=":", alpha=0.5)
            ax.tick_params(colors=self.mpl_fg)
            for spine in ax.spines.values(): spine.set_color(self.mpl_grid)
            self.fig.tight_layout()
            self.canvas.draw()
        except Exception as e:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculoVectorialMasterApp(root)
    root.mainloop()