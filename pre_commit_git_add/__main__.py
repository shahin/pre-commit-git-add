import subprocess
import sys


def main(*args, **kwargs):
    print(f"args={args}", file=sys.stderr)
    print(f"kwargs={kwargs}", file=sys.stderr)
    subprocess.run(['git', 'add', '--update'], check=True)


if __name__ == '__main__':
    raise SystemExit(main())
