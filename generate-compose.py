import argparse

import yaml


def generate_compose(start_port, end_port, delay_seconds):
    services = {}
    for i, port in enumerate(range(start_port, end_port + 1)):
        service_name = f"warp-socks-{port}"
        services[service_name] = {
            'image': 'threatpatrols/cfwarp-gost:latest',
            'restart': 'always',
            'privileged': True,
            'sysctls': [
                'net.ipv6.conf.all.disable_ipv6=0',
                'net.ipv4.conf.all.src_valid_mark=1'
            ],
            'environment': {
                'WARP_START_DELAY': i * delay_seconds
            },
            'container_name': service_name,
            'ports': [f"127.0.0.1:{port}:1080"]
        }

    compose_data = {
        'version': '3',
        'services': services
    }

    with open('docker-compose.yml', 'w') as f:
        yaml.dump(compose_data, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a docker-compose.yml file for multiple WARP SOCKS proxies.")
    parser.add_argument('--start-port', type=int, default=9000, help="The starting port for the proxy services.")
    parser.add_argument('--end-port', type=int, default=9100, help="The ending port for the proxy services.")
    parser.add_argument('--delay-seconds', type=int, default=30, help="The delay in seconds between starting each container.")
    args = parser.parse_args()

    generate_compose(args.start_port, args.end_port, args.delay_seconds)
    print(f"Successfully generated docker-compose.yml for ports {args.start_port} to {args.end_port} with a {args.delay_seconds}-second delay between each start.")
