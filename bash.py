
# import subprocess

# # Exécuter la commande 'mount' et récupérer la sortie
# output = subprocess.check_output(['mount'])

# # Parcourir les lignes de sortie pour extraire les informations de montage
# for line in output.decode('utf-8').splitlines():
#     # Extraire le nom de l'appareil et le point de montage
#     device, mountpoint = line.strip().split(' on ')
#     # Afficher les informations de montage
#     print(f"{device} est monté sur {mountpoint}")


import subprocess

# Exécuter la commande 'mount' et récupérer la sortie
mount_output = subprocess.check_output(['mount'])

# Exécuter la commande 'diskutil list' et récupérer la sortie
disk_output = subprocess.check_output(['diskutil', 'list'])

# Créer un dictionnaire pour stocker les noms de volumes par numéro de disque
volumes = {}

# Parcourir les lignes de sortie pour extraire les informations de montage
for line in mount_output.decode('utf-8').splitlines():
    # Extraire le nom de l'appareil et le point de montage
    device, mountpoint = line.strip().split(' on ')
    # Extraire le numéro de disque
    disk_number = device.split('/')[-1]
    # Ajouter le point de montage au dictionnaire de volumes
    volumes[disk_number] = mountpoint

# Parcourir les lignes de sortie pour extraire les noms de volumes
for line in disk_output.decode('utf-8').splitlines():
    # Vérifier si la ligne correspond à un disque monté
    if ' (disk' in line and 'Mounted' in line:
        # Extraire le numéro de disque et le nom de volume
        disk_number, volume_name = line.strip().split()[0:2]
        # Vérifier si nous avons des informations de montage pour ce disque
        if disk_number in volumes:
            # Afficher le nom du volume et le point de montage
            print(
                f"{volume_name} ({disk_number}) est monté sur {volumes[disk_number]}")
