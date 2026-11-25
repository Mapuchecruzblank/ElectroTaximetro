# ⚡ Electro-Taxímetro (Smart Energy Manager)

Sistema de monitoreo, simulación y gestión de consumo eléctrico doméstico orientado a IoT. Permite visualizar el gasto energético en tiempo real traducido a pesos chilenos ($ CLP), gestionar electrodomésticos, controlar presupuestos mensuales y proyectar ahorros, diseñado bajo una arquitectura web *mobile-first* (PWA) preparada para integrarse con hardware **ESP32 + sensor SCT-013**.

---

## 🛠️ Stack Tecnológico

* **Backend:** Python 3 + Django (ORM, Autenticación nativa, API REST interna)
* **Base de Datos:** SQLite3 (integrada en desarrollo; escalable a PostgreSQL/MySQL)
* **Frontend:** HTML5, CSS3 (*Mobile-First* / Responsive), JavaScript (Fetch API para actualizaciones en tiempo real) y **Chart.js** (gráficos dinámicos)
* **Hardware Futuro (Fase 2):** Microcontrolador ESP32 + Sensor de corriente no invasivo SCT-013 (100A/50mA)

---

## 📂 Estructura del Proyecto

```text
electro-taximetro/
│
├── config/                     # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── settings.py             # Configuración de apps, templates, static y SQLite
│   ├── urls.py                 # Rutas globales
│   └── wsgi.py
│
├── core/                       # Aplicación principal (Lógica de negocio y simulación)
│   ├── migrations/             # Historial de cambios en la base de datos
│   ├── templates/              # Vistas HTML diseñadas para pantalla móvil
│   │   ├── base.html           # Plantilla base con barra de navegación móvil
│   │   ├── login.html          # Inicio de sesión y registro de usuarios
│   │   ├── dashboard.html      # Taxímetro en vivo, presupuesto y gráficos
│   │   └── dispositivos.html   # Gestión y encendido/apagado de aparatos
│   │
│   ├── static/                 # Archivos estáticos
│   │   ├── css/
│   │   │   └── styles.css      # Estilos responsivos (vista tipo app móvil)
│   │   ├── js/
│   │   │   └── taximetro.js    # Lógica de polling (fetch), cálculo CLP y Chart.js
│   │   └── manifest.json       # Configuración PWA para instalar en el teléfono
│   │
│   ├── admin.py                # Registro de modelos en el panel de Django
│   ├── models.py               # Tablas: Dispositivo, LecturaConsumo, Presupuesto
│   ├── urls.py                 # Rutas de vistas y endpoints JSON (/api/...)
│   └── views.py                # Controladores de vistas, simulador y receptor ESP32
│
├── .gitignore                  # Exclusión de db.sqlite3, __pycache__ y venv
├── manage.py                   # CLI de administración de Django
├── requirements.txt            # Dependencias del proyecto (Django)
└── README.md                   # Documentación del proyecto