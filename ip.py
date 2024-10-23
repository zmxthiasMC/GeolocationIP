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

def get_phone_info(ip_address):
    # Usar Numverify API para obtener información del teléfono
    numverify_api_key = 'TU_API_KEY'
    numverify_url = f'http://apilayer.net/api/validate?access_key={numverify_api_key}&number={ip_address}'
    numverify_response = requests.get(numverify_url)
    numverify_data = numverify_response.json()
    
    phone_data = {
        "Número de Teléfono": numverify_data.get("number"),
        "Validez": numverify_data.get("valid"),
        "Formato Internacional": numverify_data.get("international_format"),
        "Formato Nacional": numverify_data.get("local_format"),
        "País": numverify_data.get("country_name"),
        "Ubicación": numverify_data.get("location"),
        "Operador": numverify_data.get("carrier"),
        "Tipo de Línea": numverify_data.get("line_type")
    }
    return phone_data

def print_info(info):
    for key, value in info.items():
        print(f"{Fore.WHITE}{key}: {Fore.GREEN}{value}")

if __name__ == "__main__":
    print_logo()
    target_ip = input(Fore.RED + ">> ")
    location_info = get_location(target_ip)
    phone_info = get_phone_info(target_ip)
    location_info.update(phone_info)
    print_info(location_info)
    
