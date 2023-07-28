To install the project you need:

Get credentials for Google API (for Google Sheets) and copy 
file named "credentials.json" in google_api_module.

Connect Postgres and Google Data Studio (Postgres IP needed)

    .env file has variables:
    POSTGRES_USER
    POSTGRES_PASSWORD
    POSTGRES_DB
    POSTGRES_HOST
    POSTGRES_PORT
    RABBITMQ_USER
    RABBITMQ_PASS
    SPREADSHEET_ID

The command to run is:
    docker-compose up --build -d
