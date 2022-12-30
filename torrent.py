import os
import tempfile

from fastapi import FastAPI
from torrentool.api import create_torrent

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to the HTML site publisher!"}

@app.post("/publish")
def publish(html: str):
    # Create a temporary directory to store the HTML files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Write the HTML content to a file
        html_path = os.path.join(tmpdir, "index.html")
        with open(html_path, "w") as f:
            f.write(html)

        # Create a torrent file for the HTML site
        torrent_path = os.path.join(tmpdir, "site.torrent")
        create_torrent(html_path, torrent_path)

        # Return the torrent file as a response
        with open(torrent_path, "rb") as f:
            return {"torrent_file": f.read()}

@app.get("/sites")
def list_sites():
    # This function should return a list of published HTML sites,
    # along with their torrent files and any other relevant information.
    return {"sites": []}

@app.get("/sites/{site_id}")
def get_site(site_id: str):
    # This function should return the information for a specific published HTML site,
    # identified by its ID.
    return {"site": {}}

@app.delete("/sites/{site_id}")
def delete_site(site_id: str):
    # This function should delete a published HTML site, identified by its ID.
    return {"message": "Site deleted successfully"}
