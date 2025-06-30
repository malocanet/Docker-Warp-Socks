# Docker-Warp-Socks

A Docker setup to expose multiple Cloudflare WARP instances as SOCKS5 proxies. This configuration is designed to provide a new IP address from Cloudflare WARP for each container.

## Quick Start

1.  **Prerequisites**: Make sure you have Python, Docker, and Docker Compose installed. You will also need the `PyYAML` and `requests` packages, which you can install with `pip install pyyaml requests`.

2.  **Generate `docker-compose.yml`**: Run the `generate-compose.py` script to create the `docker-compose.yml` file.

    ```sh
    python generate-compose.py --start-port 9000 --end-port 9100
    ```

    You can customize the port range by changing the `--start-port` and `--end-port` arguments. The script also includes a staggered start delay to avoid rate-limiting issues. You can control this with the `--delay-seconds` argument.

3.  **Start the Containers**: Once the `docker-compose.yml` file is generated, you can start all the containers with the following command:

    ```sh
    docker-compose up -d
    ```

## Check Proxies

To check the status of all the proxies, run the `check-proxies.py` script. This script will test each proxy in the specified range and print its status and IP address.

```sh
python check-proxies.py --start-port 9000 --end-port 9100
```

You can customize the port range and the number of threads for checking:

```sh
python check-proxies.py --start-port 9000 --end-port 9100 --threads 100
```

## Getting a New IP

To get a new IP address for all containers, simply restart them:

```sh
docker-compose down
docker-compose up -d
```

Each time you restart the containers, they should each get a new IP address from Cloudflare.
