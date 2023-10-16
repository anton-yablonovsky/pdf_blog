# Structure
1. Nginx - ip:80
2. Backend - ip:8000
3. Frontend - /usr/share/nginx/html

# Running dev version
1. Change ip of nginx server in frontend/config/nginx.conf (3 and 4 lines)
1. docker-compose build
2. docker-compose up -d
3. docker-compose logs -f
