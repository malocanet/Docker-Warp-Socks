FROM ubuntu:latest

# Install basic tools
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    net-tools \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Add your CloudKid specific setup here
# COPY your-app /app
# WORKDIR /app

# Expose SOCKS proxy port
EXPOSE 1080

# Add startup command
CMD ["/bin/bash"]
