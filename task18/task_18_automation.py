# -*- coding: utf-8 -*-
"""
Exercices Section 18: Connexion et Automatisation sur le Cisco Devnet Sandbox
"""

import yaml
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

# ==============================================================================
# TASK 18.1, 18.1a, 18.1b : Fonction pour envoyer une commande SHOW
# ==============================================================================
def send_show_command(device, command):
    """
    Se connecte à un équipement via SSH, exécute une commande de type SHOW,
    et gère les exceptions d'authentification et de timeout.
    """
    try:
        with ConnectHandler(**device) as ssh:
            # Sur les Sandbox Cisco, nous sommes souvent déjà en mode privilégié, 
            # mais ssh.enable() sécurise le passage si nécessaire.
            try:
                ssh.enable()
            except Exception:
                pass
            output = ssh.send_command(command)
            return output
            
    except NetmikoAuthenticationException:
        print(f"[{device.get('host')}] Erreur: Échec d'authentification (Vérifier le mot de passe).")
        return ""
        
    except NetmikoTimeoutException:
        print(f"[{device.get('host')}] Erreur: L'équipement n'est pas joignable (Timeout).")
        return ""

# ==============================================================================
# TASK 18.2, 18.2a : Fonction pour envoyer des commandes de CONFIGURATION
# ==============================================================================
def send_config_commands(device, config_commands, log=True):
    """
    Se connecte à un équipement, passe en mode configuration et exécute une liste
    de commandes. Le paramètre 'log' contrôle l'affichage des informations.
    """
    if log:
        print(f"Connecting to {device.get('host')}...")
        
    try:
        with ConnectHandler(**device) as ssh:
            try:
                ssh.enable()
            except Exception:
                pass
            output = ssh.send_config_set(config_commands)
            return output
            
    except (NetmikoAuthenticationException, NetmikoTimeoutException) as error:
        print(f"[{device.get('host')}] Impossible d'exécuter la configuration: {error}")
        return ""

# ==============================================================================
# BLOC PRINCIPAL : Exécution sur le routeur Devnet Sandbox
# ==============================================================================
if __name__ == "__main__":
    
    print("=== Exécution de la Task 18.1 (Show Command) ===")
    show_cmd = "show ip interface brief"
    
    try:
        with open("devices.yaml") as f:
            devices_list = yaml.safe_load(f)
            
        for dev in devices_list:
            print(f"\n--- Connexion établie avec : {dev.get('host')} ---")
            result_show = send_show_command(dev, show_cmd)
            if result_show:
                print(result_show)
                
    except FileNotFoundError:
        print("Erreur: Le fichier 'devices.yaml' est introuvable.")

    print("\n" + "="*60 + "\n")
    print("=== Exécution de la Task 18.2 (Configuration Commands) ===")
    
    cfg_cmds = [
        'logging buffered 20010', 
        'no logging console'
    ]
    
    for dev in devices_list:
        # Exécution de la Task 18.2 avec affichage du log de connexion (Task 18.2a)
        result_cfg = send_config_commands(dev, cfg_cmds, log=True)
        if result_cfg:
            print(result_cfg)
