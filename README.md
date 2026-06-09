# App-finanza-PyQt5

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-PyQt5-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)

Una aplicación de escritorio intuitiva y robusta para la **gestión y control de finanzas personales**, desarrollada en Python utilizando la biblioteca gráfica **PyQt5**. Esta herramienta permite a los usuarios registrar, organizar y visualizar sus flujos económicos de manera eficiente a través de una interfaz limpia y dinámica.

---

## 🚀 Características Principales

* **Registro de Flujos:** Gestión dinámica de ingresos y egresos mediante tablas interactivas.
* **Categorización Avanzada:** Clasificación de movimientos para un análisis detallado del destino del dinero.
* **Interfaz Gráfica Moderna:** Diseño intuitivo construido sobre PyQt5, optimizado para la experiencia de usuario.
* **Persistencia de Datos:** Almacenamiento eficiente para el seguimiento del historial financiero a lo largo del tiempo.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Interfaz Gráfica (GUI):** PyQt5
* **Gestión de Datos:** Componentes nativos de manejo de tablas y estructuras de datos dinámicas en Python.

---

## 📦 Instalación y Configuración

Sigue estos pasos para clonar el repositorio y ejecutar la aplicación en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/samurai-labbug/App-finanza-PyQt5.git
cd App-finanza-PyQt5
```

### 2. Crear y activar un entorno virtual (Recomendado)
En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
En macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
Asegúrate de tener `pip` actualizado e instala PyQt5:
```bash
pip install --upgrade pip
pip install PyQt5
```

---

## 💻 Uso

Para iniciar la aplicación, ejecuta el script principal desde la terminal:

```bash
python main.py
```
*(Nota: Reemplaza `main.py` por el nombre del archivo de entrada principal de tu proyecto si este difiere, por ejemplo, `app.py`).*

---

## 📂 Estructura del Proyecto

A continuación se detalla la organización de los archivos principales:

```text
App-finanza-PyQt5/
│
├── main.py              # Punto de entrada de la aplicación
├── gui/                 # Diseños de interfaz (.ui) y lógica de ventanas
│   ├── main_window.py   # Controlador de la pantalla principal
│   └── ...
├── modules/             # Lógica de negocio (cálculos, manejo de datos)
│   ├── finanzas.py
│   └── ...
└── README.md            # Documentación del proyecto
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar la aplicación, optimizar el código o añadir nuevas funciones:

1. Haz un **Fork** del proyecto.
2. Crea una nueva rama para tu característica (`git checkout -b feature/NuevaMejora`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añade nueva funcionalidad'`).
4. Sube los cambios a tu rama (`git push origin feature/NuevaMejora`).
5. Abre un **Pull Request**.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE) si está disponible.

---
**Desarrollado por [samurai-labbug](https://github.com/samurai-labbug)**
