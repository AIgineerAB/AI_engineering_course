# Ragbit

## Virtual environment structure

problem with what we've done before:
- one .venv for everything
- packages in backend are shared to frontend as well and vice versa
- we want to dockerize backend to a docker container and frontend to another docker container

goal:
inside docker container
- backend has packages for backend
- frontend has packages for frontend

to do this we need workspaces in uv

## Steps

1. `uv init --package ragbit`
2. moved backend, frontend and knowledge_base into ragbit/src/ragbit
3. modified pyproject.toml inside ragbit
4. created pyproject.toml in frontend and backend and added dependencies
5. `uv sync` to install dependencies
6. update app.py to take in API_URL
7. Dockerfile for frontend
8. Dockerfile for backend
9. write docker-compose.yaml 
10. `docker compose up -d` to build images and spin up containers
11. double check with `docker ps` to see if they are running
12. also check the container logs in docker desktop 
13. good for debugging or double checking is to jump into container
    `docker exec -it container_name bash`
14. if container has exited and you want to spin up to debug,
    `docker run -it image_name bash` 
15. To clean up containers -> do `docker compose down`, important to be in folder where your docker-compose.yaml lives
16. When updating code and you want to make sure it is in the new image, do `docker compose up -d --build`