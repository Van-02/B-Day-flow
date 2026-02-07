# 🎂 B-Day Flow: Automatización de Cumpleaños

**Idioma**

- 🇪🇸 Español
- [🇺🇸 English](./README.md)

**B-Day Flow** es una herramienta profesional de automatización en Python que sincroniza eventos de Google Calendar con WhatsApp. El sistema identifica automáticamente los cumpleaños del día desde un calendario específico y envía saludos personalizados a través de la API de Evolution API.

## 🚀 Funcionalidades Clave

- **Integración con Google Calendar:** Obtiene eventos en tiempo real usando la API de Google Discovery.
- **Mensajería Automatizada de WhatsApp:** Envío de mensajes personalizados mediante Evolution API.
- **Parsing Inteligente:** Extrae nombres de clientes, números de teléfono e información del vendedor directamente de las descripciones de los eventos.
- **Testing Robusto:** Incluye una suite completa de pruebas unitarias con Mocks para asegurar la estabilidad sin depender de APIs externas.
- **Configuración Centralizada:** Gestión segura de variables de entorno y tiempos de reintento.

## 🛠️ Stack Tecnológico

- **Lenguaje:** [Python 3.14+](www.python.org)
- **APIs:** [Google Calendar API v3](https://developers.google.com/workspace/calendar/api/guides/overview?hl=es-419), [Evolution API](https://github.com/EvolutionAPI/evolution-api)
- **Testing:** [Pytest](https://docs.pytest.org/en/stable/index.html)

## 📦 Estructura del Proyecto

```text
BdayFlow/
├── tests/              # Pruebas unitarias para servicios y helpers
├── utils/              # Helpers de formateo y expresiones regulares (Regex)
├── calendar_service.py # Lógica de conexión con Google Calendar
├── whatsapp_client.py  # Integración con la API de WhatsApp
├── config.py           # Administrador central de configuración
├── main.py             # Orquestador principal de ejecución
└── templates.py        # Plantillas de mensajes personalizados
```

## 🐳 Despliegue con Docker

1. Construir y levantar la imagen.

```Bash
docker-compose up -d --build
```

1. Google Auth

La primera vez, el contenedor necesitará que te loguees en Google. Revisá los logs para ver el link de autenticación

```Bash
docker logs -f bday-flow
```

_Nota: Asegurate de tener `credentials.json` en la raiz antes de empezar._

## ⚙️ Configuración e Instalación

1. **Clonar el repositorio:**

```Bash
git clone https://github.com/Van-02/bday-flow.git
cd bday-flow
```

1. **Crear y activar un entorno virtual:**

```Bash
python -m venv venv
source venv/bin/activate
```

1. **Instalar dependencias:**

```Bash
pip install -r requirements.text
```

1. **Configurar Variables de Entorno:** Creá un archivo `.env` en el directorio raiz:

```Code
AUTHENTICATION_API_KEY=Tu_api_de_evolution
GOOGLE_CALENDAR_ID=tu_id_de_calendario@group.calendar.google.com
```

1. **Credenciales de Google API:** Colocá tu archivo `credentials.json` (obtenido desde Google Cloud Console) en la raiz. El archivo `token.json` se generará automáticamente después del primer inicio de sesión.

## 🧪 Ejecución de Tests

Para verificar que todo esté funcionando correctamente antes de lanzar a producción:

```Bash
python -m pytest -v
```
