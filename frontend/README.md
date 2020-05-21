# VueJS docker Template

> VueJS template project with production docker support

## Build Setup

- Without Docker (standalone)
``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# serve for production at 0.0.0.0:8080
npm run serve

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

- With Docker

```bash
docker build -t image-tag:latest .
docker run --rm --init -e DEBUG=1 -p 8080:8080 image-tag:latest
```

- With docker-compose

```bash
docker-compose up --build -d
# OR only frontend
docker-compose build frontend
docker-compose up -d
```
