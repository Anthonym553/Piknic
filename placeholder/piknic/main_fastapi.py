from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from piknic.modules.mapbox import get_locations
from piknic.models import Location_Post
import os

app = FastAPI()

# Allow CORS for all origins
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the API endpoint for getting the locations of food places within a certain radius of a given location
@app.post("/maps/get_all_locations/")
async def api_loc(latlng: Location_Post):
    return get_locations(latlng.lat, latlng.lng, latlng.radius)

# Push index file
@app.get("/")
def read_root():
    return FileResponse(os.path.dirname(os.path.realpath(__file__)) + '/static/index.html')

# Push map file
@app.get("/map")
def read_root():
    return FileResponse(os.path.dirname(os.path.realpath(__file__)) + '/static/map.html')

# Push styles
@app.get("/style")
def read_root():
    return FileResponse(os.path.dirname(os.path.realpath(__file__)) + '/static/styles/style.css')

# Push piknicLogo
@app.get("/piknicLogo")
def read_root():
    return FileResponse(os.path.dirname(os.path.realpath(__file__)) + '/static/assets/piknicLogo.jpg')

# Push new logo
@app.get("/LogoNew")
def read_root():
    return FileResponse(os.path.dirname(os.path.realpath(__file__)) + '/static/assets/LogoNew.png')

# Push video
@app.get("/video")
def read_root():
    return FileResponse(os.path.dirname(os.path.realpath(__file__)) + '/static/assets/video.mp4')
