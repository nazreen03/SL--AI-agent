import sys
import argparse
import uvicorn
import subprocess
from app.config import settings
from app.logger import logger

def start_api(host: str = "127.0.0.1", port: int = 8000):
    logger.info(f"Starting FastAPI server on http://{host}:{port}")
    uvicorn.run("api.main:app", host=host, port=port, reload=True)

def start_frontend(port: int = 8501):
    logger.info(f"Starting Streamlit UI on http://localhost:{port}")
    cmd = [sys.executable, "-m", "streamlit", "run", "frontend/app.py", "--server.port", str(port)]
    subprocess.run(cmd)

def main():
    parser = argparse.ArgumentParser(description="Self-Learning AI Agent Entry Point")
    parser.add_argument("--api", action="store_true", help="Run FastAPI API server")
    parser.add_argument("--frontend", action="store_true", help="Run Streamlit UI")
    parser.add_argument("--host", default="127.0.0.1", help="API Host")
    parser.add_argument("--port", type=int, default=8000, help="API Port")
    args = parser.parse_args()

    if args.frontend:
        start_frontend()
    elif args.api or len(sys.argv) == 1:
        start_api(host=args.host, port=args.port)

if __name__ == "__main__":
    main()
