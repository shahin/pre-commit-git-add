import subprocess
import sys


def main(*args, **kwargs):
    print(f"sys.argv={sys.argv}", file=sys.stderr)
    subprocess.run(['git', 'add', '--update'], check=True)
