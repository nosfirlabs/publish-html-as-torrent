
# HTML Site Publisher

This project provides a simple API for publishing HTML sites using BitTorrent.

## Prerequisites

-   Python 3.6 or higher
-   pip

## Installation

To install the dependencies for this project, run the following command:

`pip install -r requirements.txt` 

## Usage

To start the server, run the following command:

`python app.py` 

The API will be available at `http://localhost:8000`.

### Endpoints

-   `POST /publish`: Publish an HTML site. The request body should contain the HTML content. The server will respond with a torrent file that can be used to download the HTML site.
    
-   `GET /sites`: Get a list of all published HTML sites, along with their torrent files and any other relevant information.
    
-   `GET /sites/{site_id}`: Get the information for a specific published HTML site, identified by its ID.
    
-   `DELETE /sites/{site_id}`: Delete a published HTML site, identified by its ID.

### Notes

The `/sites` endpoint returns a list of all published HTML sites, along with their torrent files and any other relevant information. The `/sites/{site_id}` endpoint returns the information for a specific published HTML site, identified by its ID. The `/sites/{site_id}` endpoint deletes a published HTML site, identified by its ID.

