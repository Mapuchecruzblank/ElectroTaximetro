# ⚡ Electro-Taxímetro (Smart Energy Manager)

Aplicación web para registrar electrodomésticos y simular el consumo y su costo en pesos chilenos. El panel calcula el costo estimado a partir de la potencia registrada y la tarifa del perfil del usuario. La telemetría ESP32/SCT-013 es una integración futura; el proyecto actual no recibe mediciones del hardware.

---

## 🛠️ Stack Tecnológico

* **Backend:** Python 3 y Django 6.1.3, con ORM y autenticación de Django.
* **Base de datos:** SQLite (`db.sqlite3`) por defecto en desarrollo local. Cuando existe `DATABASE_URL`, Django usa la conexión configurada con `dj-database-url`; en producción está previsto PostgreSQL alojado en Neon.
* **Frontend:** Plantillas Django, HTML y CSS responsivo; JavaScript integrado en las plantillas del panel y Chart.js cargado desde CDN.
* **Despliegue:** Render, con Gunicorn como servidor WSGI y WhiteNoise para servir archivos estáticos.
* **PWA:** `core/static/manifest.json` declara los metadatos de instalación y `core/templates/sw.js` se sirve en `/sw.js`. El Service Worker actual no implementa caché ni funcionamiento sin conexión.

La aplicación permite crear cuentas, agregar y eliminar dispositivos, cambiar su estado y visualizar una estimación simulada del costo y la potencia. Aunque existe el modelo `LecturaConsumo`, el panel actual calcula la simulación en el navegador y no tiene un endpoint de telemetría ESP32.

---

## 📂 Estructura del Proyecto

```text
ElectroTaximetro/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── img/
│   │   │   └── icon-512.png
│   │   ├── js/                  # Directorio vacío actualmente
│   │   └── manifest.json
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── landing.html
│   │   ├── login.html
│   │   ├── registro.html
│   │   └── sw.js
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

`db.sqlite3` se crea localmente al ejecutar las migraciones y está excluida del repositorio por `.gitignore`.

---

## 💻 Instalación y ejecución local

Requisitos: Python 3 y Git. En Linux o macOS:

```bash
git clone https://github.com/Mapuchecruzblank/ElectroTaximetro.git
cd ElectroTaximetro
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`. Si no se define `DATABASE_URL`, Django utilizará SQLite en `db.sqlite3`. En Windows, activa el entorno virtual con `venv\Scripts\activate` en lugar de `source venv/bin/activate`.

---

## 🚀 Despliegue en Render

Para un despliegue con PostgreSQL en Neon, configura la conexión de Neon como `DATABASE_URL` en las variables de entorno del servicio Render. El servicio puede instalar las dependencias con `pip install -r requirements.txt`, ejecutar `python manage.py migrate` y arrancar con:

```bash
gunicorn config.wsgi:application
```

WhiteNoise está incluido en el middleware; `STATIC_ROOT` está configurado para la recopilación de archivos estáticos.

### Variables de entorno

En un entorno de producción se deben usar:

* `DATABASE_URL`: URL de conexión de PostgreSQL en Neon.
* `SECRET_KEY`: clave secreta de Django, generada y guardada como secreto en Render; no debe publicarse en el repositorio.
* `DEBUG`: debe estar desactivado (`False`) en producción.

**Nota sobre la configuración actual:** `config/settings.py` solo lee `DATABASE_URL`. `SECRET_KEY` está definida directamente en el archivo y `DEBUG` permanece en `True`; esas dos opciones todavía no se cargan desde variables de entorno. Por lo tanto, definirlas en Render no surtirá efecto hasta adaptar la configuración de Django. No se incluye aquí ningún valor secreto.
