# VueJS frontend

## Setup

1.  Start the recommendor portal project with docker-compose
2.  Copy the env.example to .env running the following <br />

    ```bash
    $ cp -rv env.example .env
    ```

3.  Go to `localhost:8000/api/core/login` and login using CAS, you will recieve a token, add that to .env created in step 2
4.  Install the dependicies in frontend by going into folder and running `npm install`
5.  Start the frontend by running the following

    ```bash
    $ DEBUG=1 ./entrypoint.sh
    ```

    Your app would be running at `localhost:8080`

## Add dummy items in db

Go to `localhost:8000/db_interface` after starting the recommender portal project

If you have recieved the token as told earlier. you will see a `core` database inside that you will find your user object inside users collections.

To add a dummy item

1. Create a db with your the categoryId.
2. Create a collection named data inside the db
3. Add your item to collection

The item schema can be found by going to `localhost:8000/api/redoc` inside the add item route documentation. The request body schema for each item is shown properly.
