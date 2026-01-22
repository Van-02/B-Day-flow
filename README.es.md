# 🎂 B-Day Flow: Automatización de Cumpleaños

**Idioma**

- 🇪🇸 Español
- [🇺🇸 English](./README.md)

**B-Day Flow** es una herramienta profesional de automatización en Python que sincroniza eventos de Google Calendar con WhatsApp. El sistema identifica automáticamente los cumpleaños del día desde un calendario específico y envía saludos personalizados a través de la API de Whapi.Cloud.

## 🚀 Funcionalidades Clave

- **Integración con Google Calendar:** Obtiene eventos en tiempo real usando la API de Google Discovery.
- **Mensajería Automatizada de WhatsApp:** Envío de mensajes personalizados mediante Whapi Cloud.
- **Parsing Inteligente:** Extrae nombres de clientes, números de teléfono e información del vendedor directamente de las descripciones de los eventos.
- **Testing Robusto:** Incluye una suite completa de pruebas unitarias con Mocks para asegurar la estabilidad sin depender de APIs externas.
- **Configuración Centralizada:** Gestión segura de variables de entorno y tiempos de reintento.

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.14+
- **APIs:** Google Calendar API v3, Whapi.Cloud
- **Testing:** Pytest
- **Entorno:** Dotenv para gestión de secretos

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
WHAPI_TOKEN=tu_token_de_whapi_aqui
WHAPI_URL=[https://gate.whapi.cloud/messages/text](https://gate.whapi.cloud/messages/text)
GOOGLE_CALENDAR_ID=tu_id_de_calendario@group.calendar.google.com
```

1. **Credenciales de Google API:** Colocá tu archivo `credentials.json` (obtenido desde Google Cloud Console) en la raiz. El archivo `token.json` se generará automáticamente después del primer inicio de sesión.

## 🧪 Ejecución de Tests

Para verificar que todo esté funcionando correctamente antes de lanzar a producción:

```Bash
python -m pytest -v
```
