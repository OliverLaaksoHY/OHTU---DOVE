# OHTU---DOVE

## Link to OKD: 
[App in OKD](https://route-ohjelmistotuotanto-lahiopetus-2026-14.ext.okd-cs-test-0.k8s.cs.helsinki.fi)
## Team rules:
[Team rules](https://github.com/OliverLaaksoHY/OHTU---DOVE/blob/main/pelisaannot.md)
## Product and sprint backlogs:
[Product backlog](https://github.com/users/OliverLaaksoHY/projects/1/)

[Sprint 1 backlog](https://github.com/users/OliverLaaksoHY/projects/1/views/4)

[Sprint 2 backlog](https://github.com/users/OliverLaaksoHY/projects/1/views/5)

# How to run

## 1. Clone

````bash
git clone git@github.com:OliverLaaksoHY/OHTU---DOVE.git
cd OHTU---DOVE
````

## 2. When running the first time, you need to setup the database and env

````bash
uv sync
cp .env.example .env
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

## 5. To run robot tests you additionally need to run

````bash
uv run rfbrowser install chromium
bash run_robot_tests.sh
````
