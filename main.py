
from app.routes import create_app
from app.config import ConfigEnv
import uvicorn


config = ConfigEnv()
app = create_app(config)


if __name__ == "__main__":
    

    uvicorn.run(app, host="127.0.0.1", port=9090)
