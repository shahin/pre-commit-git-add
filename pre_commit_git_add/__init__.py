import subprocess
import sys


def main():
    print(f"sys.argv={sys.argv}", file=sys.stderr)
    subprocess.run(['git', 'add', *sys.argv[1:]], check=True)
