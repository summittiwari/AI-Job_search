# Dockerfile for React frontend (Create React App)
FROM node:20-alpine AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Serve static build with a simple web server
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
