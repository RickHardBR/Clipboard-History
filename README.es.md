# 📋 Clipboard History Manager

<p align="center">
  <a href="README.md">Português</a> | <a href="README.en.md">English</a> | <b>Español</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Versión de Python" />
  <img src="https://img.shields.io/badge/GUI-Tkinter%20%7C%20ttkbootstrap-darkgreen" alt="Framework GUI" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white" alt="Plataforma" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="Licencia" />
</p>

Un gestor de historial del portapapeles moderno, rápido y ligero para **Windows**, desarrollado en **Python** con **Tkinter** y **ttkbootstrap**.

Monitorea automáticamente todo lo que copias (textos, enlaces y capturas de pantalla), organízalo por pestañas con un diseño elegante, edita elementos al instante y personaliza temas e idiomas con actualización en tiempo real sin reiniciar.

---

## ✨ Características Principales

- 🔄 **Monitoreo Continuo del Portapapeles**: Captura automática de textos copiados, enlaces web e imágenes sin interrumpir tu flujo de trabajo.
- 🗂️ **Categorización Inteligente en Pestañas**:
  - **Textos**: Historial de textos convencionales copiados.
  - **Enlaces**: Detección y separación automática de URLs web (`http://` y `https://`).
  - **Imágenes**: Historial con miniaturas, fecha, hora y hash de archivo.
- 🎨 **Interfaz Moderna y Pulida**:
  - Componentes personalizados en Canvas (`RoundedButton`, `CustomTabBar`, `CustomList`) con esquinas redondeadas, transiciones suaves al pasar el ratón y selección activa en forma de *pill*.
  - Barras de desplazamiento discretas integradas a la paleta de colores.
  - Soporte completo para **Modo Oscuro (Dark)** y **Modo Claro (Light)**.
  - 4 Colores de Énfasis (*Accent Colors*): **Púrpura**, **Verde azulado**, **Azul** y **Rojo**.
- 🌐 **Soporte Multilenguaje (i18n)**:
  - 🇧🇷 Português (Brasil)
  - 🇺🇸 English
  - 🇪🇸 Español
- ⚡ **Hot-Reload en Tiempo Real**: Cambia temas, colores de énfasis o idiomas y visualiza toda la interfaz actualizarse al instante, **sin necesidad de reiniciar**.
- 🖼️ **4 Modos de Visualización de Imágenes**:
  - Detalles (Lista con fecha, hora y hash)
  - Iconos Pequeños (64x64)
  - Iconos Medianos (128x128)
  - Iconos Grandes (256x256)
- ✏️ **Editor Rápido Integrado**: Ventana emergente para inspeccionar y editar textos sobre la marcha.
- 💾 **Exportación a TXT**: Guarda cualquier texto o enlace seleccionado directamente en un archivo `.txt`.
- 🗑️ **Papelera de Reciclaje**: Elimina elementos con seguridad, con opción de restaurar o eliminar definitivamente.

---

## 🛠️ Tecnologías Utilizadas

- **[Python 3.12](https://www.python.org/)** — Lenguaje principal.
- **Tkinter** — Framework nativo de interfaz gráfica.
- **[ttkbootstrap](https://ttkbootstrap.readthedocs.io/)** — Temas modernos y estilos para widgets ttk.
- **[Pillow (PIL)](https://python-pillow.org/)** — Captura, procesamiento y renderizado de imágenes del portapapeles.
- **[PyInstaller](https://pyinstaller.org/)** — Empaquetado en un ejecutable `.exe` independiente para Windows.

---

## 📂 Estructura del Proyecto

```plaintext
Clipboard History/
│
├── .gitignore             # Reglas de exclusión de Git
├── clipboard_history.py   # Código fuente principal de la aplicación
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación en portugués
├── README.en.md           # Documentación en inglés
└── README.es.md           # Documentación en español (actual)
```

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos Previos

Asegúrate de tener instalado **Python 3.10 o superior** en tu sistema.

### 1. Clonar el repositorio

```bash
git clone https://github.com/RickHardBR/Clipboard-History.git
cd Clipboard-History
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

```bash
python clipboard_history.py
```

---

## 📦 Cómo Generar el Ejecutable (.exe)

Puedes compilar el programa en un único archivo ejecutable independiente para Windows:

Ejecuta el siguiente comando en la raíz del proyecto:

```powershell
pyinstaller --onefile --windowed --name "ClipboardHistory" clipboard_history.py
```

El binario resultante se encontrará en:
```
dist/ClipboardHistory.exe
```

> **Nota:** El parámetro `--windowed` garantiza que la aplicación se inicie en modo ventana sin abrir una consola de comandos de fondo.

---

## ⚙️ Configuración y Preferencias

Las preferencias se guardan de forma persistente en el archivo `config.json`:

```json
{
    "theme": "dark",
    "accent_color": "#7c5cff",
    "language": "es_ES"
}
```

Para modificar los ajustes:
1. Abre **Configuración > Preferencias** en la barra de menú superior.
2. Elige el **Tema Visual**, el **Color de Énfasis** y el **Idioma**.
3. Haz clic en **Aplicar y Guardar**. ¡Los cambios se aplicarán de inmediato!

---

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE). Puedes usarlo, modificarlo y distribuirlo libremente.

---

<p align="center">
  Desarrollado por <b>RickHardBR</b> 🚀
</p>
