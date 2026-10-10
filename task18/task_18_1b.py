# -*- coding: utf-8 -*-
"""
Task 18.1b : Gestion complète des exceptions (Authentification & Timeout)
"""
import yaml
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            return ssh.send_command(command)
    except NetmikoAuthenticationException:
        print(f"[{device.get('host')}] Erreur: Échec d'authentification (Vérifier le mot de passe).")
        return ""
    except NetmikoTimeoutException:
        print(f"[{device.get('host')}] Erreur: L'équipement n'est pas joignable (Timeout réseau).")
        return ""

if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        
    for dev in devices:
        print(f"\n--- Exécution de la Task 18.1b sur : {dev.get('host')} ---")
        send_show_command(dev, command)
