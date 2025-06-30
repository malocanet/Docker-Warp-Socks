import argparse
import subprocess
import time


def run_containers(quantity):
    for i in range(quantity):
        port = 54700 + i
        name = f"wasque{i+1}"
        command = [
            "docker", "run", "-d",
            "--name", name,
            "--rm",
            "--privileged",
            "--sysctl", "net.ipv6.conf.all.disable_ipv6=0",
            "--sysctl", "net.ipv4.conf.all.src_valid_mark=1",
            "-p", f"{port}:1080",
            "cloudkid:latest"
        ]
        subprocess.run(command)
        print(f"Started container {name} on port {port}")
        if i < quantity - 1:
            time.sleep(30)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run multiple Docker containers with a delay.")
    parser.add_argument('quantity', type=int, help="The number of containers to run.")
    args = parser.parse_args()

    run_containers(args.quantity)    