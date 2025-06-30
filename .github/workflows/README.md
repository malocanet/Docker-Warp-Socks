# CloudKid Container GitHub Actions

This directory contains GitHub Actions workflows for running CloudKid containers.

## Workflows

### 1. cloudkid-containers.yml (Basic)
- Automatically runs on push/PR to main branch
- Starts 10 CloudKid containers by default
- 30-second delay between container starts
- Basic health checking

### 2. cloudkid-containers-advanced.yml (Advanced)
- Manual trigger with customizable options
- Configurable number of containers (1-20)
- Health checks for each container
- Container logs collection
- Network connectivity testing
- Resource usage monitoring
- Optional cleanup

## Usage

### Basic Workflow
The basic workflow runs automatically on:
- Push to main/master branch
- Pull requests to main/master branch

### Advanced Workflow (Recommended)
1. Go to Actions tab in your repository
2. Select "Run CloudKid Containers (Advanced)"
3. Click "Run workflow"
4. Configure options:
   - **Number of containers**: 1, 5, 10, 15, or 20
   - **Keep running minutes**: How long to keep containers running
   - **Cleanup after**: Whether to stop containers after completion

## Container Configuration
Each container:
- Name format: `wasque{number}`
- Port mapping: `54700+index:1080`
- Privileged mode enabled
- IPv6 enabled
- 30-second startup delay between containers

## Security Notes
- Never commit API keys or tokens to the repository
- Use GitHub Secrets for sensitive data
- The GITHUB_TOKEN is automatically provided for registry access

## Monitoring
- Container status is displayed during workflow execution
- Logs are collected and uploaded as artifacts
- Resource usage (CPU/Memory) is monitored
- Network connectivity is tested

## Troubleshooting
1. **Container fails to start**: Check the container logs in the artifacts
2. **Health check fails**: Verify the service is running on port 1080
3. **Port conflicts**: Ensure ports 54700-54719 are not in use

## Local Testing
To test locally before pushing:
```bash
# Run the Python script
python cloudkidx.py 10

# Or use Docker directly
docker run -d --name wasque1 --rm --privileged \
  --sysctl net.ipv6.conf.all.disable_ipv6=0 \
  --sysctl net.ipv4.conf.all.src_valid_mark=1 \
  -p 54700:1080 cloudkid:latest
```