# 420-4Q5-TP3-2355128-2438375

# NOMS et DA
Cedric SADIE 2438375
Leslie TENANG 2355128

# Url de depot GitHub
https://github.com/Leslietenang/420-4Q5-TP3-2355128-2438375.git

# adresse ip
vm1: 192.168.10.10
vm2: 192.168.10.11
# commandes de déploiement
docker compose up -d --build

# test de l'etat des conteneurs
docker compose ps

# afficher les logs du conteneur de maintenance
docker logs maintenance

# Effectuer la sauvegarde depuis vm1:
docker compose up maintenance

# vérifier la présence des sauvegardes sur VM2
ssh auto2@192.168.10.11 (adresse dynamique 172.20.45.67)
ls -l /srv/backups/tp3