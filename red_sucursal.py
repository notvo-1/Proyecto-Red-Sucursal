#!/usr/bin/env python3
"""
SISTEMA INTEGRAL DE GESTIÓN DE RED - SUCURSAL
Autores: Mati, Lucas, Santi y Martin
Fecha: Octubre 2025
Descripción: Sistema unificado para automatización de configuración de red
"""

import datetime
import os
import json
import platform

class GestorRedSucursal:
    def __init__(self):
        self.nombre_proyecto = "Red Sucursal - Implementación"
        self.archivo_log = "logs/operaciones_red.log"
        self.crear_estructura_directorios()
        
        # CONFIGURACIÓN BASE DE LA RED (tu configuración actual)
        self.configuracion_red = {
            "vlans": [
                {"id": 10, "nombre": "ADMINISTRACION", "puertos": ["Gig1/0/4"], "descripcion": "Personal administrativo"},
                {"id": 20, "nombre": "VENTAS", "puertos": ["Gig1/0/1", "Gig1/0/2", "Gig1/0/3"], "descripcion": "Departamento de ventas"},
                {"id": 30, "nombre": "SOPORTE", "puertos": [], "descripcion": "Equipo de soporte técnico"},
                {"id": 40, "nombre": "SERVIDORES", "puertos": [], "descripcion": "Servidores internos"},
                {"id": 99, "nombre": "MANAGEMENT", "puertos": ["Gig1/0/10", "Gig1/0/11"], "descripcion": "Gestión de dispositivos"}
            ],
            "dispositivos": [
                {"nombre": "Router0", "tipo": "Router", "ip": "192.168.1.1", "vlan": 99},
                {"nombre": "Switch0", "tipo": "Switch Core", "ip": "192.168.1.2", "vlan": 99},
                {"nombre": "Switch1", "tipo": "Switch Acceso", "ip": "192.168.1.3", "vlan": 99},
                {"nombre": "Server0", "tipo": "Servidor", "ip": "10.10.40.10", "vlan": 40},
                {"nombre": "Server1", "tipo": "Servidor", "ip": "10.10.40.11", "vlan": 40}
            ]
        }
    
    def crear_estructura_directorios(self):
        """Crea la estructura de directorios del proyecto"""
        directorios = ["configs", "docs/reportes", "logs"]
        for directorio in directorios:
            os.makedirs(directorio, exist_ok=True)
    
    def log_operacion(self, mensaje):
        """Registra operaciones en el archivo de log"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.archivo_log, 'a', encoding='utf-8') as log:
            log.write(f"[{timestamp}] {mensaje}\n")
    
    def mostrar_estado_actual(self):
        """Muestra el estado actual de la red de forma clara"""
        print("\n" + "="*70)
        print("                   ESTADO ACTUAL DE LA RED")
        print("="*70)
        
        print("\n VLANs CONFIGURADAS:")
        print("-" * 50)
        for vlan in self.configuracion_red["vlans"]:
            estado_puertos = f"{len(vlan['puertos'])} puertos" if vlan['puertos'] else "SIN PUERTOS ⚠️"
            print(f"  VLAN {vlan['id']:2} | {vlan['nombre']:15} | {estado_puertos:15} | {vlan['descripcion']}")
            if vlan['puertos']:
                print(f"          Puertos: {', '.join(vlan['puertos'])}")
        
        print(f"\n ACCIONES REQUERIDAS:")
        print("  - Asignar puertos a VLAN 30 (SOPORTE)")
        print("  - Asignar puertos a VLAN 40 (SERVIDORES)")
        
        self.log_operacion("Usuario consultó estado actual de la red")
    
    def generar_comandos_vlans(self, solo_return = True): #podria reutilizarse
        """Genera comandos Cisco para crear VLANs"""
        print("\n GENERANDO COMANDOS PARA CREAR VLANs")
        print("-" * 40)
        
        comandos = []
        comandos.append("! =========================================")
        comandos.append("! COMANDOS PARA CREACIÓN DE VLANs")
        comandos.append("! =========================================")
        comandos.append("configure terminal")
        """"Segmento posiblemente reutilizable"""
        for vlan in self.configuracion_red["vlans"]:
            comandos.append(f"vlan {vlan['id']}")
            comandos.append(f" name {vlan['nombre']}")
            comandos.append("!")
        
        comandos.append("end")
        comandos.append("! =========================================")
        
        # Mostrar comandos en pantalla
        for comando in comandos:
            print(comando)
        
        self.log_operacion("Generados comandos de creación de VLANs")
        return comandos #PODRIAMOS ELMINAR LOS RETURNS O USARLOS EN COMPLETAR_CONMFIGURACION
    
    def generar_comandos_puertos(self):
        """Genera comandos para asignar puertos a VLANs"""
        print("\n GENERANDO COMANDOS PARA ASIGNAR PUERTOS")
        print("-" * 45)
        
        comandos = []
        comandos.append("! =========================================")
        comandos.append("! COMANDOS PARA ASIGNACIÓN DE PUERTOS")
        comandos.append("! =========================================")
        comandos.append("configure terminal")
        
        # Asignaciones específicas para tu red
        asignaciones = [
            ("Gig1/0/22", 30, "PC-SOPORTE"),
            ("Gig1/0/24", 40, "SERVER1")
        ]
        
        for puerto, vlan_id, dispositivo in asignaciones:
            comandos.append(f"interface {puerto}")
            comandos.append(" switchport mode access")
            comandos.append(f" switchport access vlan {vlan_id}")
            comandos.append(" spanning-tree portfast")
            comandos.append(f"! Conectado a: {dispositivo}")
            comandos.append("!")
        
        # Puertos trunk (conexiones entre switches)
        comandos.append("interface Gig1/0/23")
        comandos.append(" switchport mode trunk")
        comandos.append(" switchport trunk native vlan 99")
        comandos.append("! Puerto trunk - Conexión entre switches")
        comandos.append("!")
        
        comandos.append("end")
        comandos.append("copy running-config startup-config")
        comandos.append("! =========================================")
        
        for comando in comandos:
            print(comando)
        
        self.log_operacion("Generados comandos de asignación de puertos")
        return comandos #PODRIAMOS ELMINAR LOS RETURNS O USARLOS EN COMPLETAR_CONMFIGURACION
    
    def completar_configuracion_automatica(self):
        """Completa automáticamente la configuración faltante"""
        print("\n COMPLETANDO CONFIGURACIÓN AUTOMÁTICAMENTE")
        print("-" * 45)
        
        # Actualizar la configuración interna
        for vlan in self.configuracion_red["vlans"]:
            if vlan["id"] == 30 and not vlan["puertos"]:
                vlan["puertos"].append("Gig1/0/22")
                print(f"✅ Asignado Gig1/0/22 a VLAN 30 (SOPORTE)")
            
            if vlan["id"] == 40 and not vlan["puertos"]:
                vlan["puertos"].append("Gig1/0/24")
                print(f"✅ Asignado Gig1/0/24 a VLAN 40 (SERVIDORES)")
        
        print("\n CONFIGURACIÓN COMPLETADA:")
        print("   - VLAN 30 (SOPORTE) ahora tiene: Gig1/0/22")
        print("   - VLAN 40 (SERVIDORES) ahora tiene: Gig1/0/24")
        
        self.log_operacion("Configuración automática completada")
    
    def generar_reporte_completo(self):
        """Genera un reporte completo en archivo de texto"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"docs/reportes/reporte_red_{timestamp}.txt"
        
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("="*70 + "\n")
            archivo.write("           REPORTE COMPLETO DE CONFIGURACIÓN DE RED\n")
            archivo.write("="*70 + "\n")
            archivo.write(f"Proyecto: {self.nombre_proyecto}\n")
            archivo.write(f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            archivo.write("Generado automáticamente por el sistema de gestión\n")
            archivo.write("="*70 + "\n\n")
            
            # Sección VLANs
            archivo.write("VLANS CONFIGURADAS:\n")
            archivo.write("-" * 50 + "\n")
            for vlan in self.configuracion_red["vlans"]:
                archivo.write(f"VLAN {vlan['id']}: {vlan['nombre']}\n")
                archivo.write(f"  Descripción: {vlan['descripcion']}\n")
                archivo.write(f"  Puertos: {', '.join(vlan['puertos']) if vlan['puertos'] else 'Ninguno'}\n\n")
            
            # Sección comandos
            archivo.write("\nCOMANDOS PARA IMPLEMENTACIÓN:\n")
            archivo.write("-" * 40 + "\n")
            archivo.write("! Copiar y pegar en Cisco Packet Tracer\n\n")
            
            comandos_vlan = self.generar_comandos_vlans()
            comandos_puertos = self.generar_comandos_puertos()
            
            for comando in comandos_vlan + [""] + comandos_puertos:
                archivo.write(comando + "\n")
        
       
            for cmd in comandos_vlan:
                archivo.write(cmd + "\n") 
                
            archivo.write("\n")  

            for cmd in comandos_puertos:
                archivo.write(cmd + "\n") 
        return nombre_archivo
    
    
    def verificar_configuracion(self):
        """Verifica que la configuración sea correcta"""
        print("\n VERIFICANDO CONFIGURACIÓN")
        print("-" * 30)
        
        problemas = []
        
        # Verificar VLANs sin puertos
        for vlan in self.configuracion_red["vlans"]:
            if not vlan["puertos"] and vlan["id"] not in [1, 1002, 1003, 1004, 1005]:
                problemas.append(f"VLAN {vlan['id']} ({vlan['nombre']}) no tiene puertos asignados")
        
        # Mostrar resultados
        if not problemas:
            print(" Configuración OK - Todas las VLANs tienen puertos asignados")
        else:
            print("  Se encontraron problemas:")
            for problema in problemas:
                print(f"   - {problema}")
        
        print("\n COMANDOS DE VERIFICACIÓN EN PACKET TRACER:")
        print("   show vlan brief          - Ver VLANs y puertos")
        print("   show interfaces status   - Ver estado de puertos")
        print("   show running-config      - Ver configuración completa")
        
        self.log_operacion("Verificación de configuración realizada")

def main():
    """Función principal con menú interactivo"""
    sistema = GestorRedSucursal()
    
    print(" SISTEMA DE GESTIÓN DE RED - SUCURSAL")
    print("   Automatización de configuración Cisco")
    print("="*50)
    
    while True:
        
        limpiar_consola()
        print("\n MENÚ PRINCIPAL:")
        print("   1.  Mostrar estado actual de la red")
        print("   2.  Generar comandos para VLANs")
        print("   3.  Generar comandos para puertos")
        print("   4.  Completar configuración automáticamente")
        print("   5.  Generar reporte completo")
        print("   6.  Verificar configuración")
        print("   7.  Salir")
        print("-" * 40)
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            sistema.mostrar_estado_actual()
        
        elif opcion == "2":
            sistema.generar_comandos_vlans()
        
        elif opcion == "3":
            sistema.generar_comandos_puertos()
        
        elif opcion == "4":
            sistema.completar_configuracion_automatica()
        
        elif opcion == "5":
            archivo = sistema.generar_reporte_completo()
            print(f"\n ¡Reporte listo! Copia los comandos a Packet Tracer")
        
        elif opcion == "6":
            sistema.verificar_configuracion()
        
        elif opcion == "7":
            print("\n👋 ¡Hasta luego! Recuerda:")
            print("   - Usar los comandos generados en Packet Tracer")
            print("   - Verificar la configuración con 'show vlan brief'")
            print("   - Revisar los reportes en la carpeta 'docs/reportes/'")
            break
        
        else:
            print("❌ Opción no válida. Por favor, seleccione 1-7.")
        
        input("\nPresione Enter para continuar...")
        
def limpiar_consola():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()