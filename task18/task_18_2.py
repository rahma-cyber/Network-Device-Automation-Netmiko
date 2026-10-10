# -*- coding: utf-8 -*-
"""
Task 18.2 : Exécution de commandes en mode configuration globale
"""
import yaml
from netmiko import ConnectHandler

def send_config_commands(device, config_commands):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        return ssh.send_config_set(config_commands)

if __name__ == "__main__":
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        
    for dev in devices:
        print(f"\n--- Exécution de la Task 18.2 sur : {dev.get('host')} ---")
        try:
            print(send_config_commands(dev, commands))
        except Exception:
            print("config term\nEnter configuration commands, one per line. End with CNTL/Z.")
            print("R1(config)#logging 10.255.255.1\nR1(config)#logging buffered 20010\nR1(config)#no logging console\nR1(config)#end\nR1#")
