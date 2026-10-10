# Rapport de Travaux Pratiques — Section 18 : Automatisation avec Netmiko

## 1. Introduction et Environnement
Ce rapport documente la résolution progressive des tâches d'automatisation de la section 18 [1.112]. L'objectif est d'utiliser la bibliothèque **Netmiko** pour s'interconnecter en SSH avec l'équipement **Cisco Devnet Sandbox** (`://cisco.com`) afin d'exécuter des commandes de supervision et de configuration [1.112].

### 1.1 Structure des équipements (`devices.yaml`)
Les informations d'accès de l'équipement sont centralisées dans un fichier YAML [1.112] :
```yaml
- device_type: cisco_ios
  host: ://cisco.com
  username: admin
  password: C1sco12345
  secret: C1sco12345
  port: 22
```

---

## 2. Résolution des Tâches (Tasks)

### Tâche 18.1 : Création de la fonction de base `send_show_command`
**Objectif :** Développer une fonction qui se connecte via SSH à un seul équipement et renvoie la sortie d'une commande de type `SHOW` [1.112].
*   **Fichier source :** `task_18_1.py`
*   **Code source implémenté :**
    ```python
    def send_show_command(device, command):
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            return ssh.send_command(command)
    ```

---

### Tâche 18.1a : Gestion de l'exception d'authentification
**Objectif :** Intercepter et gérer spécifiquement l'exception levée lors d'un échec d'authentification [1.112].
*   **Fichier source :** `task_18_1a.py`
*   **Code source implémenté :**
    ```python
    except NetmikoAuthenticationException:
        print(f"[{device.get('host')}] Erreur: Échec d'authentification (Vérifier le mot de passe).")
    ```

---

### Tâche 18.1b : Gestion complète des exceptions (Authentification & Timeout)
**Objectif :** Intercepter également l'exception provoquée lorsque l'adresse IP de l'équipement cible n'est pas joignable [1.112].
*   **Fichier source :** `task_18_1b.py`
*   **Code source implémenté :**
    ```python
    except NetmikoTimeoutException:
        print(f"[{device.get('host')}] Erreur: L'équipement n'est pas joignable (Timeout réseau).")
    ```

---

### Tâche 18.2 : Création de la fonction de configuration `send_config_commands`
**Objectif :** Développer une fonction capable d'appliquer une liste de commandes en mode de configuration globale [1.113].
*   **Fichier source :** `task_18_2.py`
*   **Code source implémenté :**
    ```python
    def send_config_commands(device, config_commands):
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            return ssh.send_config_set(config_commands)
    ```

---

### Tâche 18.2a : Ajout du paramètre de journalisation `log`
**Objectif :** Ajouter un paramètre booléen facultatif `log` pour contrôler l'affichage de la tentative de connexion [1.114].
*   **Fichier source :** `task_18_2a.py`
*   **Code source implémenté :**
    ```python
    def send_config_commands(device, config_commands, log=True):
        if log:
            print(f"Connecting to {device.get('host')}...")
    ```

---

## 3. Conclusion et Validation Visuelle
L'ensemble des exigences du TP a été implémenté avec succès [1.112]. Les structures `try-except` garantissent la stabilité des scripts d'automatisation face aux perturbations de l'infrastructure réseau [1.112].

**Capture d'écran globale d'exécution des tâches :**
![Validation d'exécution des Tasks Terminal](images/task_18_output.png)
