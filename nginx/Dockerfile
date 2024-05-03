# Nginx Dockerfile
FROM nginx:latest

# Remove default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY default.conf /etc/nginx/conf.d/

#
COPY index.html /etc/nginx/html/

# Expose port
EXPOSE 80
