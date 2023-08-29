from lib.repository import Repository
import sys

creating = len(sys.argv) == 2 and sys.argv[1] == "create"

repositories = [
    Repository("/home/rileymathews/server", "/mnt/disk1/backups/server"),
    Repository("/mnt/md0/volumes/gitea", "/mnt/disk1/backups/gitea"),
    Repository("/mnt/md0/volumes/homeassistant", "/mnt/disk1/backups/homeassistant"),
    Repository("/mnt/md0/volumes/mastodon", "/mnt/disk1/backups/mastodon"),
    Repository("/mnt/md0/volumes/pihole", "/mnt/disk1/backups/pihole"),
    Repository("/mnt/md0/volumes/vaultwarden", "/mnt/disk1/backups/vaultwarden"),
    Repository("/mnt/md0/volumes/nextcloud", "/mnt/disk1/backups/nextcloud")
]

for repo in repositories:
    if creating:
        repo.create()
    else:
        repo.backup()
