## Run Steps Locally using Docker

1. Install Docker on your machine if you haven't already. You can download it from the official Docker website.

2. Clone the repository to your local machine

3. Navigate to the project directory:

    ```bash
    cd medivise
    ```

4. Create an .env file with 

```bash
DATABRICKS_HOST=
DATABRICKS_TOKEN=
MONGO_URI=
MONGO_DB=
MONGO_COLLECTION_NAME=
ATLAS_VECTOR_SEARCH_INDEX_NAME=
```
5. Install python dependencies. Please have installed poetry.

```bash
poetry install
```

6. Run application
```bash
poetry run python -m medivise
```

7. Open your web browser and visit `http://localhost:8002/docs` to access the application.

