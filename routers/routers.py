from fastapi import APIRouter

page_router = APIRouter()

@page_router.get('/')
async def home():
    return {'message':'This is the home page'}

@page_router.get('/about')
async def about():
    return {'message':'This is the about page'}

