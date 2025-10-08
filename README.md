==================================================
PROYECTO RED SUCURSAL - SISTEMA DE AUTOMATIZACIÓN
==================================================

Este proyecto implementa un SISTEMA DE AUTOMATIZACIÓN Y GENERACIÓN DE
COMANDOS CISCO, diseñado para optimizar la configuración, gestión de VLANs
y documentación de la infraestructura de red en Cisco Packet Tracer.

--------------------------------------------------
CARACTERÍSTICAS CLAVE
--------------------------------------------------

- GENERADOR DE COMANDOS: Crea scripts de configuración listos para la CLI.
- GESTIÓN DE VLANs: Administración centralizada de la segmentación de red.
- REPORTES AUTOMÁTICOS: Genera documentación técnica profesional.
- INTERFAZ INTUITIVA: Menú interactivo en consola.

--------------------------------------------------
ESTRUCTURA DEL PROYECTO
--------------------------------------------------

proyecto_red/
├── scripts/
│   └── red_sucursal.py    # <--- Script principal
├── docs/reportes/         # Documentación generada
├── configs/               # Archivos de configuración Cisco (output)
├── logs/                  # Registros de eventos
└── README.md              # Documentación del repositorio

--------------------------------------------------
CONFIGURACIÓN DE VLANs
--------------------------------------------------

El sistema gestiona la siguiente segmentación de red:

| ID | Nombre         | Propósito
|----|----------------|-------------------------------------
| 10 | ADMINISTRACION | Personal administrativo y gerencial.
| 20 | VENTAS         | Departamento de ventas.
| 30 | SOPORTE        | Equipo de soporte técnico.
| 40 | SERVIDORES     | Servidores internos y aplicaciones.
| 99 | MANAGEMENT     | Gestión de dispositivos de red.

--------------------------------------------------
USO E IMPLEMENTACIÓN
--------------------------------------------------

1. REQUISITOS:
   El sistema requiere **Python 3.8+**.

2. EJECUCIÓN:
   Para iniciar, navega al directorio raíz y ejecuta:
   $ python scripts/red_sucursal.py

3. APLICACIÓN EN PACKET TRACER:
   - Usa el menú para generar los comandos.
   - Copia la salida del script.
   - Pega los comandos en la CLI de los dispositivos en Packet Tracer.
   - Verifica la configuración con el comando 'show vlan brief'.

--------------------------------------------------
AUTORES
--------------------------------------------------

Proyecto desarrollado por: Mati, Lucas, Santi, y Martin.