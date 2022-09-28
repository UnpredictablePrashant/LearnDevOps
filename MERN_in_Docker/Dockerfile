# Production Build

# Stage 1: Build react client
FROM node:16 as frontend

# Working directory be app
WORKDIR /usr/app/backend/

COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# copy local files to app folder
COPY frontend/ ./
RUN ls

RUN npm run build

# Stage 2 : Build Server

FROM node:16

WORKDIR /usr/src/app/
COPY --from=frontend /usr/app/frontend/build/ ./frontend/build/
RUN ls

WORKDIR /usr/src/app/backend/
COPY backend/package*.json ./
RUN npm install -qy
COPY backend/ ./

ENV PORT 3001

EXPOSE 3001

CMD ["npm", "start"]