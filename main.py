from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import random

app = FastAPI()

templates = Jinja2Templates(directory="templates")

with open('./data/baits.json', 'r') as json_file:
    baits = json.load(json_file)

with open('./static/routes.json', 'r') as json_file:
    dynamic_routes = json.load(json_file)


def add_dynamic_routes(app: FastAPI, route_dict: dict):
    for route_id, route_data in route_dict.items():
        route_path = route_data["path"]

        @app.get(route_path, response_class=HTMLResponse)
        async def dynamic_route(request: Request, route_id=route_id):
            bait = baits[str(route_id)]
            title = bait[0]
            response = bait[1]
            return templates.TemplateResponse(
                "route.html",
                {"request": request, "title": title, "response": response},
            )



def generate_routes_from_baits(count: int = 1) -> dict:
    selected_routes = {}
    selected_ids = random.sample(list(baits.keys()), count)

    for route_id in selected_ids:
        route_path = f"/{random.randint(1000, 9999)}"
        selected_routes[route_id] = {"path": route_path}

    return selected_routes


@app.on_event("startup")
async def setup_routes():
    new_routes = generate_routes_from_baits(count=1)
    dynamic_routes.update(new_routes)
    add_dynamic_routes(app, dynamic_routes)

    # Save updated routes to a file for reference
    with open('./static/routes.json', 'w') as fp:
        json.dump(dynamic_routes, fp)


# Static root route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "routes": dynamic_routes, "baits": baits}
    )