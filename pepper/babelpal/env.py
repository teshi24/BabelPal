import os

def load_dotenv(filepath):
    with open(filepath) as f:
        for line in f:
            # Strip whitespace and ignore comments or empty lines
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Split key and value
            key, value = line.split('=', 1)
            os.environ[key.strip()] = value.strip()