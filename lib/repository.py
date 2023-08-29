import subprocess

class Repository:
    local_path: str
    remote_path: str
    remote_host: str
    remote_user: str

    def __init__(
        self,
        local_path: str,
        remote_path: str,
        remote_host: str = '10.0.0.36',
        remote_user: str = 'rileymathews'
    ):
        self.local_path = local_path
        self.remote_path = remote_path
        self.remote_host = remote_host
        self.remote_user = remote_user

    def exists(self) -> bool:
        command = f"restic -r {self.repository_string} cat config"
        try:
            subprocess.check_output(command, shell=True, text=True)
            return True
        except Exception as e:
            return False

    def create(self):
        if not self.exists():
            print(f"creating repository {self.repository_string}")
            command = f"restic -r {self.repository_string} init"
            subprocess.check_output(command, shell=True, text=True)
        else:
            print(f"repository {self.repository_string} already exists") 

    @property
    def repository_string(self):
        return f"sftp:{self.remote_user}@{self.remote_host}:{self.remote_path}"
    
    def backup(self):
        command = f"restic -r {self.repository_string} --verbose backup {self.local_path}"
        print(f"running {command}")
        print(subprocess.check_output(command, shell=True, text=True))
