FROM caddy

EXPOSE 8080

# Set the working directory
WORKDIR /srv

# Start Caddy
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
