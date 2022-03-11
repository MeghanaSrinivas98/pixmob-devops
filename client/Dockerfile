FROM node:alpine
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
COPY ./ ./
RUN yarn add @material-ui/core @material-ui/icons react-router-dom sweetalert
RUN npm i
CMD ["yarn", "start"]
