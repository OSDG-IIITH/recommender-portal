# Recommender System IIIT-H

- Pydantic-based models
- Fast

## Installation

```
cp -rv env.example .env  # populate with your own values
docker-compose up -d
```

(_Note: read up on resources mentioned on Slack for debugging help_)

## Routes

### Static files

The `nginx` service serves both static files from the front and backend.

Add staticfiles for
- frontend: to the `rollup` build process OR to
`frontend/dist/`
- backend: to `backend/static`

### API

The `backend` service is to be accessed from the frontend using `/api` prefix.

Thus any backend routes are now `/api/route-to-be-accessed`. Because of this,
the API docs are hosted at `/api/docs`.

### DB Interface

For easy debugging purposes, there is an express mongodb interface provided at
`/db_interface/`. This will probably be obselete since the actual courier portal
database is probably going to be mySQL, but has been included for now for easy
testing
