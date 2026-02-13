import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

## Variables
REPO_URL = "https://github.com/atakan-erdonmez/knowledge-base.git"
BACKUP_DIR = Path("/var/backups/knowledge_base")
REPO_NAME = "knowledge_base"
KEEP_COUNT = 5


def run_backup():
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_filename = f"{REPO_NAME}_{date_str}"
    temp_clone_dir = BACKUP_DIR / "temp_clone"
    
    if not BACKUP_DIR.exists():
        BACKUP_DIR.mkdir(parents=True)
        
        
    try:
        print(f"Cloning {REPO_URL}..")
        subprocess.run(['git', 'clone', REPO_URL, str(temp_clone_dir)], check=True)
        
        archive_path = BACKUP_DIR / zip_filename
        shutil.make_archive(str(archive_path),'zip', temp_clone_dir)
        print(f"Created archive: {zip_filename}.zip")
        
        
    finally:
        if temp_clone_dir.exists():
            shutil.rmtree(temp_clone_dir)
            
    rotate_backups()
    
def rotate_backups():
    backups = sorted(
        BACKUP_DIR.glob(f"{REPO_NAME}_*.zip"),
        key=os.path.getmtime,
        reverse=True
    )
    
    if len(backups) > KEEP_COUNT:
        for old_backup in backups[KEEP_COUNT:]:
            print(f"Deleting old backup: {old_backup.name}")
            old_backup.unlink()
            
if __name__ == "__main__":
    run_backup()
