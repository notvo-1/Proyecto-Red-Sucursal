Proyecto Red Sucursal - Sistema de Automatización
Sistema de automatización para configuración de redes Cisco - Generador de comandos y documentación para implementación en Packet Tracer.

Características Principales
Generador de Comandos Cisco: Crea configuraciones listas para Packet Tracer

Gestión de VLANs: Administra VLANs de administración, usuarios, servidores

Reportes Automáticos: Genera documentación técnica

Interfaz Intuitiva: Menú interactivo fácil de usar

Estructura del Proyecto
text
proyecto_red/
├── scripts/red_sucursal.py     # Sistema principal
├── docs/reportes/              # Reportes generados
├── configs/                    # Configuraciones
├── logs/                       # Registros
└── README.md
Configuración de VLANs
El sistema gestiona estas VLANs:

VLAN 10: ADMINISTRACION - Personal administrativo

VLAN 20: VENTAS - Departamento de ventas

VLAN 30: SOPORTE - Equipo de soporte técnico

VLAN 40: SERVIDORES - Servidores internos

VLAN 99: MANAGEMENT - Gestión de dispositivos

Instalación y Uso
Ejecutar el sistema:

bash
python scripts/red_sucursal.py
Seguir el menú interactivo para generar configuraciones

Funcionalidades
Estado de Red: Visualiza VLANs y puertos configurados

Generador de Comandos: Crea configuraciones Cisco listas para usar

Configuración Automática: Completa asignaciones faltantes

Reportes: Genera documentación profesional

Verificación: Valida la configuración propuesta

Uso con Packet Tracer
Generar comandos con el script

Copiar y pegar en Packet Tracer

Verificar con show vlan brief

Autores
Mati

Lucas

Santi

Martin

Proyecto para Tecnicatura Universitaria en Programación.