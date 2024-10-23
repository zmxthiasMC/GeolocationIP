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

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    return response.json()["ip"]

def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    location_data = {
        "ip": ip_address,
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country_name"),
        "postal": data.get("postal"),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "isp": data.get("org"),
        "timezone": data.get("timezone"),
        "languages": data.get("languages"),
        "currency": data.get("currency"),
        "mobile_provider": data.get("carrier"),
        "continent": data.get("continent_code"),
        "country_code": data.get("country_code"),
        "asn": data.get("asn"),
        "organization": data.get("org"),
        "connection_speed": data.get("connection_speed"),
        "connection_type": data.get("connection_type"),
        "ip_range": data.get("ip_range"),
        "security": data.get("security"),
        "reputation": data.get("reputation"),
        "whois": data.get("whois"),
        "demographics": data.get("demographics"),
        "weather": data.get("weather"),
        "historical_ip": data.get("historical_ip"),
        "network_info": data.get("network_info"),
        "android_version": data.get("android_version"),
        "android_bits": data.get("android_bits"),
        "device_type": data.get("device_type"),
        "os": data.get("os"),
        "browser": data.get("browser"),
        "browser_version": data.get("browser_version"),
        "screen_resolution": data.get("screen_resolution"),
        "user_agent": data.get("user_agent"),
        "vpn": data.get("vpn"),
        "proxy": data.get("proxy"),
        "tor": data.get("tor"),
        "mobile": data.get("mobile"),
        "hosting": data.get("hosting"),
        "abuse": data.get("abuse"),
        "threat_level": data.get("threat_level"),
        "threat_types": data.get("threat_types"),
        "phone_brand": data.get("phone_brand"),
        "phone_model": data.get("phone_model"),
        "phone_os": data.get("phone_os"),
        "phone_os_version": data.get("phone_os_version"),
        "phone_bits": data.get("phone_bits"),
        "battery_level": data.get("battery_level"),
        "charging_status": data.get("charging_status"),
        "network_operator": data.get("network_operator"),
        "sim_operator": data.get("sim_operator"),
        "device_manufacturer": data.get("device_manufacturer"),
        "device_model": data.get("device_model"),
        "device_id": data.get("device_id"),
        "device_serial": data.get("device_serial"),
        "device_imei": data.get("device_imei"),
        "device_meid": data.get("device_meid"),
        "device_imsi": data.get("device_imsi"),
        "device_mac": data.get("device_mac"),
        "device_ip": data.get("device_ip"),
        "device_wifi_ssid": data.get("device_wifi_ssid"),
        "device_wifi_bssid": data.get("device_wifi_bssid")
    }
    return location_data

def get_phone_info():
    response = requests.get('https://lookups.twilio.com/v2/PhoneNumbers/{phone_number}?Type=carrier&Type=caller-name')
    data = response.json()
    phone_data = {
        "phone_brand": data.get("brand"),
        "phone_model": data.get("model"),
        "phone_os": data.get("os"),
        "phone_os_version": data.get("os_version"),
        "phone_bits": data.get("bits"),
        "battery_level": data.get("battery_level"),
        "charging_status": data.get("charging_status"),
        "network_operator": data.get("network_operator"),
        "sim_operator": data.get("sim_operator"),
        "device_manufacturer": data.get("device_manufacturer"),
        "device_model": data.get("device_model"),
        "device_id": data.get("device_id"),
        "device_serial": data.get("device_serial"),
        "device_imei": data.get("device_imei"),
        "device_meid": data.get("device_meid"),
        "device_imsi": data.get("device_imsi"),
        "device_mac": data.get("device_mac"),
        "device_ip": data.get("device_ip"),
        "device_wifi_ssid": data.get("device_wifi_ssid"),
        "device_wifi_bssid": data.get("device_wifi_bssid")
    }
    return phone_data

if __name__ == "__main__":
    print_logo()
    target_ip = input(Fore.RED + ">> ")
    location_info = get_location(target_ip)
    phone_info = get_phone_info()
    location_info.update(phone_info)
    print(location_info)
    
