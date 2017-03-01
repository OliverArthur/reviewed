FROM node:7

# Install dred-ui tools
RUN npm install -g \
    gulp

# Our application directory
RUN mkdir -p /var/www/dred-ui
WORKDIR /var/www/dred-ui

# Copy src to the container
COPY . /var/www/dred-ui

# Copy entrypoint script to the container
COPY docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

EXPOSE 3000

ENTRYPOINT ["/docker-entrypoint.sh"]
