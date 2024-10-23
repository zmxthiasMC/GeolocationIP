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
    print(Fore.RED + "Ingrese las IPs del objetivo (separadas por comas):")

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

def get_phone_info(ip_address):
    # Usar Numverify API para obtener información del teléfono
    numverify_api_key = 'TU_API_KEY'
    numverify_url = f'http://apilayer.net/api/validate?access_key={numverify_api_key}&number={ip_address}'
    numverify_response = requests.get(numverify_url)
    numverify_data = numverify_response.json()

    # Usar Twilio Lookup API para obtener información adicional del teléfono
    twilio_api_key = 'TU_API_KEY'
    twilio_url = f'https://lookups.twilio.com/v2/PhoneNumbers/{ip_address}?Type=carrier&Type=caller-name'
    twilio_headers = {
        'Authorization': f'Bearer {twilio_api_key}'
    }
    twilio_response = requests.get(twilio_url, headers=twilio_headers)
    twilio_data = twilio_response.json()

    phone_data = {
        "Marca del Teléfono": twilio_data.get("carrier", {}).get("name"),
        "Modelo del Teléfono": twilio_data.get("caller_name", {}).get("caller_name"),
        "Sistema Operativo del Teléfono": twilio_data.get("os"),
        "Versión del Sistema Operativo del Teléfono": twilio_data.get("os_version"),
        "Bits del Teléfono": twilio_data.get("bits"),
        "Nivel de Batería": twilio_data.get("battery_level"),
        "Estado de Carga": twilio_data.get("charging_status"),
        "Operador de Red": twilio_data.get("network_operator"),
        "Operador de SIM": twilio_data.get("sim_operator"),
        "Fabricante del Dispositivo": twilio_data.get("device_manufacturer"),
        "Modelo del Dispositivo": twilio_data.get("device_model"),
        "ID del Dispositivo": twilio_data.get("device_id"),
        "Número de Serie del Dispositivo": twilio_data.get("device_serial"),
        "IMEI del Dispositivo": twilio_data.get("device_imei"),
        "MEID del Dispositivo": twilio_data.get("device_meid"),
        "IMSI del Dispositivo": twilio_data.get("device_imsi"),
        "MAC del Dispositivo": twilio_data.get("device_mac"),
        "IP del Dispositivo": twilio_data.get("device_ip"),
        "SSID del WiFi del Dispositivo": twilio_data.get("device_wifi_ssid"),
        "BSSID del WiFi del Dispositivo": twilio_data.get("device_wifi_bssid")
    }
    return phone_data

def print_info(info):
    for key, value in info.items():
        if value:
            print(f"{Fore.WHITE}{key}: {Fore.GREEN}{value}")

if __name__ == "__main__":
    print_logo()
    target_ips = input(Fore.RED + ">> ").split(',')
    for ip in target_ips:
        ip = ip.strip()
        location_info = get_location(ip)
        phone_info = get_phone_info(ip)
        location_info.update(phone_info)
        print_info(location_info)
    
