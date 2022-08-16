import subprocess
import sys


def main():
    subprocess.run(['git', 'add', *sys.argv[1:]], check=True)
