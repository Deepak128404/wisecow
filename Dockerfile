FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat-openbsd && \
    ln -s /usr/games/cowsay /usr/bin/cowsay && \
    ln -s /usr/games/fortune /usr/bin/fortune && \
    apt-get clean

WORKDIR /app
COPY wisecow.sh /app/wisecow.sh
RUN sed -i 's/\r$//' /app/wisecow.sh && chmod +x /app/wisecow.sh

EXPOSE 4499

CMD ["./wisecow.sh"]