from fastapi import FastAPI
from random import randint
from typing import Dict
import json

app = FastAPI()

# Dictionary to store dynamically generated routes

with open('./test.json') as json_file:
    dynamic_routes = json.load(json_file)



def add_dynamic_routes(app: FastAPI, route_dict: Dict[int, str]):
    """
    Adds routes dynamically to the FastAPI app.

    Args:
        app (FastAPI): The FastAPI application instance.
        route_dict (Dict[int, str]): Dictionary mapping route keys to route paths.
    """
    for route_id, route_path in route_dict.items():
        @app.get(route_path)
        async def dynamic_route(id=route_id):
            return {"message": f"This is page {id}"}


def generate_random_routes(count: int = 1) -> Dict[int, str]:
    """
    Generates a dictionary of random routes.

    Args:
        count (int): Number of random routes to generate (default is 1).

    Returns:
        Dict[int, str]: Dictionary of generated routes.
    """
    return {randint(0, 9999): f"/{randint(0, 9999)}" for _ in range(count)}


# Add existing or dynamically generated routes during application startup
@app.on_event("startup")
async def setup_routes():
    # Generate 5 random routes as an example
    new_routes = generate_random_routes(count=5)
    dynamic_routes.update(new_routes)
    add_dynamic_routes(app, dynamic_routes)
    print("Dynamic routes added:")
    for route_id, route_path in new_routes.items():
        print(f"Route ID: {route_id}, Path: {route_path}")

    with open('test.json', 'w') as fp:
        json.dump(dynamic_routes, fp)


print(dynamic_routes)
