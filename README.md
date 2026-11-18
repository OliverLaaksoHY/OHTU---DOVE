# OHTU---DOVE

# How to run

## 1. Clone

````bash
git clone git@github.com:OliverLaaksoHY/OHTU---DOVE.git
cd OHTU---DOVE
````

## 2. When running the first time, you need to setup the database

````bash
uv sync
uv run python src/db_helper.py
uv run python src/index.py
````

## 3. After first run you can just run the program

````bash
uv sync
uv run python src/index.py
````

## 4. Access app

````bash
Use browser to view http://127.0.0.1:5001
````
