from fastapi import FastAPI, HTTPException, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import json

from app.config import ConfigEnv
from app.setlist.generate import generate_setlist
from app.spotify.generate import generate_playlist

load_dotenv()


def create_app(config: ConfigEnv):

    app = FastAPI()
    templates = Jinja2Templates(directory="templates")

    @app.get("/", response_class=HTMLResponse)
    async def read_root(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})


    @app.post("/create-playlist", response_class=HTMLResponse)
    async def display_setlist(
        request: Request,
        artist_name: str = Form(...),
        playlist_flag: str = Form(...),
    ):

        spotify_setlist = generate_setlist(
            config.setlist_connector(),
            artist_name,
            playlist_flag
        )

        response = templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "spotify_setlist": spotify_setlist,
                "artist_name": artist_name,
            },
        )
        spotify_setlist_json = json.dumps(spotify_setlist)
        response.set_cookie(key="artist_name", value=artist_name)
        response.set_cookie(key="spotify_setlist_json", value=spotify_setlist_json)
        return response

    @app.get("/login")
    async def login():
        """
        Redirects the user to the Spotify authorization URL.
        """
        try:
            auth_url = config.spotify_auth().get_authorize_url()
            return RedirectResponse(auth_url)
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
        


    @app.get("/callback")
    async def callback(request: Request, response: Response):
        code = request.query_params.get("code")
        if not code:
            raise HTTPException(status_code=400, 
                                detail="Authorization code not found")
        try:
            token_info = config.spotify_auth().get_authorize_token(code)
            spotify_connection = config.spotify_auth().get_spotify_client(
                token_info
            )

            # Retrieve the cookie containing the list of songs
            spotify_setlist_json = request.cookies.get("spotify_setlist_json")
            spotify_setlist = json.loads(spotify_setlist_json)
            if not spotify_setlist:
                raise HTTPException(
                    status_code=400, 
                    detail="Cookie 'spotify_setlist_json' not found"
                )

            # Retrieve artist_name from the cookie
            artist_name = request.cookies.get("artist_name")
            if not artist_name:
                artist_name = "Unknown Artist"  # Fallback if not found

            playlist_url = generate_playlist(
                spotify_connection,
                config.spotify_user(),
                artist_name,
                spotify_setlist
            )

            return templates.TemplateResponse(
                "success.html", {"request": request, 
                                 "playlist_url": playlist_url})
                                 
                               
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    return app
