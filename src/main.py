import uvicorn
from backend.app import app
import webbrowser
from threading import Timer


def open_browser():
	webbrowser.open_new(f"http://localhost:{3000}")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    uvicorn.run(app, host="127.0.0.1", port=3000)
