import os
import tarfile
import subprocess
from datetime import datetime
from pathlib import Path
 
SAUVEGARDE = "/archives"
 
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nomArchive = f"backup_{timestamp}.tar.gz"
cheminArchive = os.path.join(SAUVEGARDE, nomArchive)
 

 
with tarfile.open(cheminArchive, "w:gz") as tar:
    tar.add("/backup/wordpress", arcname="wordpress")
    tar.add("/backup/db", arcname="db")
 
size = os.path.getsize(cheminArchive) / (1024 * 1024)
 
 
destination = f"{os.getenv("BACKUP_USER")}@{os.getenv("BACKUP_HOST")}:{os.getenv("BACKUP_PATH")}"
 
 
subprocess.run([
    "rsync",
    "-avz",
    cheminArchive,
    destination
], check=True)
 
 
for file in Path(SAUVEGARDE).glob("backup_*.tar.gz"):
    
    nbreJours = (datetime.now().timestamp() - file.stat().st_mtime) / 86400
 
    if nbreJours  > 7:
        file.unlink()
 

 