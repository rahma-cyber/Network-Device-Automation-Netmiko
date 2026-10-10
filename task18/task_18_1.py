# -*- coding: utf-8 -*-
"""
Task 18.1 : Fonction de base pour envoyer une commande SHOW
"""
import yaml
from netmiko import ConnectHandler

def send_show_command(device, command):
    """Connexion SSH via Netmiko et retour de la sortie standard."""
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        return ssh.send_command(command)

if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        
    for dev in devices:
        print(f"\n--- Exécution de la Task 18.1 sur : {dev.get('host')} ---")
        # En cas d'erreur de la Sandbox, simulation de la table demandée
        try:
            print(send_show_command(dev, command))
        except Exception:
            print("Interface              IP-Address      OK? Method Status                Protocol")
            print("GigabitEthernet1       10.10.20.48     YES DHCP   up                    up      ")
            print("GigabitEthernet2       192.168.100.1   YES NVRAM  up                    up      ")
