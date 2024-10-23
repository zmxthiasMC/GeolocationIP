import requests
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def print_logo():
    logo = """
    ███████╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
    ██╔════╝██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
    █████╗  ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
    ██╔══╝  ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
    ██║     ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
    """
    print(Fore.RED + logo)
    print(Fore.RED + "Ingrese la IP del objetivo:")

def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    location_data = {
        "IP": ip_address,
        "Ciudad": data.get("city"),
        "Región": data.get("region"),
        "País": data.get("country_name"),
        "Código Postal": data.get("postal"),
        "Latitud": data.get("latitude"),
        "Longitud": data.get("longitude"),
        "ISP": data.get("org"),
        "Zona Horaria": data.get("timezone"),
        "Idiomas": data.get("languages"),
        "Moneda": data.get("currency"),
        "Proveedor Móvil": data.get("carrier"),
        "Continente": data.get("continent_code"),
        "Código de País": data.get("country_code"),
        "ASN": data.get("asn"),
        "Organización": data.get("org"),
        "Velocidad de Conexión": data.get("connection_speed"),
        "Tipo de Conexión": data.get("connection_type"),
        "Rango de IP": data.get("ip_range"),
        "Seguridad": data.get("security"),
        "Reputación": data.get("reputation"),
        "WHOIS": data.get("whois"),
        "Demografía": data.get("demographics"),
        "Clima": data.get("weather"),
        "Historial de IP": data.get("historical_ip"),
        "Información de Red": data.get("network_info"),
        "Versión de Android": data.get("android_version"),
        "Bits de Android": data.get("android_bits"),
        "Tipo de Dispositivo": data.get("device_type"),
        "Sistema Operativo": data.get("os"),
        "Navegador": data.get("browser"),
        "Versión del Navegador": data.get("browser_version"),
        "Resolución de Pantalla": data.get("screen_resolution"),
        "Agente de Usuario": data.get("user_agent"),
        "VPN": data.get("vpn"),
        "Proxy": data.get("proxy"),
        "TOR": data.get("tor"),
        "Móvil": data.get("mobile"),
        "Hosting": data.get("hosting"),
        "Abuso": data.get("abuse"),
        "Nivel de Amenaza": data.get("threat_level"),
        "Tipos de Amenaza": data.get("threat_types")
    }
    return location_data

def get_phone_info(phone_number):
    api_key = 'TU_API_KEY'
    url = f'https://lookups.twilio.com/v2/PhoneNumbers/{phone_number}?Type=carrier&Type=caller-name'
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    phone_data = {
        "Marca del Teléfono": data.get("carrier", {}).get("name"),
        "Modelo del Teléfono": data.get("caller_name", {}).get("caller_name"),
        "Sistema Operativo del Teléfono": data.get("os"),
        "Versión del Sistema Operativo del Teléfono": data.get("os_version"),
        "Bits del Teléfono": data.get("bits"),
        "Nivel de Batería": data.get("battery_level"),
        "Estado de Carga": data.get("charging_status"),
        "Operador de Red": data.get("network_operator"),
        "Operador de SIM": data.get("sim_operator"),
        "Fabricante del Dispositivo": data.get("device_manufacturer"),
        "Modelo del Dispositivo": data.get("device_model"),
        "ID del Dispositivo": data.get("device_id"),
        "Número de Serie del Dispositivo": data.get("device_serial"),
        "IMEI del Dispositivo": data.get("device_imei"),
        "MEID del Dispositivo": data.get("device_meid"),
        "IMSI del Dispositivo": data.get("device_imsi"),
        "MAC del Dispositivo": data.get("device_mac"),
        "IP del Dispositivo": data.get("device_ip"),
        "SSID del WiFi del Dispositivo": data.get("device_wifi_ssid"),
        "BSSID del WiFi del Dispositivo": data.get("device_wifi_bssid")
    }
    return phone_data

def print_info(info):
    for key, value in info.items():
        print(f"{Fore.WHITE}{key}: {Fore.GREEN}{value}")

if __name__ == "__main__":
    print_logo()
    target_ip = input(Fore.RED + ">> ")
    location_info = get_location(target_ip)
    phone_number = input(Fore.RED + "Ingrese el número de teléfono del objetivo (con código de país): ")
    phone_info = get_phone_info(phone_number)
    location_info.update(phone_info)
    print_info(location_info)
    
