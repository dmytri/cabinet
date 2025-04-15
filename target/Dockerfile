FROM caddy:alpine
EXPOSE 80

RUN mkdir -p /srv && echo "hello world" > /srv/index.html
WORKDIR /srv

CMD ["caddy", "file-server", "--root", "/srv", "browse"]


