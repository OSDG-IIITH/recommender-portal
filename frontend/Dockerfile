FROM node:8-alpine
LABEL author=pk13055 version=1.0

ARG DEBUG=1
ENV DEBUG=$DEBUG

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY package*.json ./

USER node
RUN npm install --save-dev

COPY --chown=node:node . .

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
