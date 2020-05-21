FROM node:8-alpine
LABEL author=pk13055 version=1.0

ARG DEBUG=1
ARG NODE_ENV=development

ENV NODE_ENV=$NODE_ENV
ENV DEBUG=$DEBUG
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=/home/node/.npm-global/bin:$PATH
ENV PATH=/home/node/app/node_modules/.bin:$PATH
 
## Install build toolchain, install node deps and compile native add-ons
RUN apk add --no-cache python make g++

USER node
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app

COPY package*.json ./
RUN npm install --save-dev
COPY --chown=node:node . .

EXPOSE 8080
ENTRYPOINT ["./entrypoint.sh"]
