from fastapi import FastAPI
from routers.routers import page_router
from random import randint

app = FastAPI()


# This can be replaced with a JSON file with the generated prompts
dynamic_routes = {}  


def include_router(app):
    app.include_router(page_router)


def add_random_route(app, random_number):
    @app.get(f"/{random_number}")
    async def random_page():
        return {"message": f"This is page {random_number}"}

    dynamic_routes[random_number] = f"/{random_number}"


def start_application():
    app = FastAPI()
    include_router(app)
    # The number is generated here
    random_number = randint(0, 9999)
    add_random_route(app, random_number)
    print(f"New route added: /{random_number}")

    return app


app = start_application()
