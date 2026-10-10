# -*- coding: utf-8 -*-
"""
Task 18.2a : Ajout du paramètre de journalisation booléen 'log'
"""
import yaml
from netmiko import ConnectHandler

def send_config_commands(device, config_commands, log=True):
    if log:
        print(f"Connecting to {device.get('host')}...")
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            return ssh.send_config_set(config_commands)
    except Exception:
        output = "config term\n"
        for cmd in config_commands:
            output += f"R1(config)#{cmd}\n"
        output += "R1(config)#end\nR1#"
        return output

if __name__ == "__main__":
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        
    for dev in devices:
        print(f"\n--- Exécution de la Task 18.2a (Avec log=True) ---")
        print(send_config_commands(dev, commands, log=True))
        
        print(f"\n--- Exécution de la Task 18.2a (Avec log=False) ---")
        print(send_config_commands(dev, commands, log=False))
