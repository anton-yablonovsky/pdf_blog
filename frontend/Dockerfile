FROM node:lts-alpine as build
RUN mkdir frontend
ADD ./ /frontend
WORKDIR /frontend/
RUN npm install
RUN npm run build
FROM nginx:1.13
RUN rm -rf /usr/share/nginx/html/*
COPY ./config/nginx.conf /etc/nginx/conf.d/
COPY --from=build /frontend/dist /usr/share/nginx/html