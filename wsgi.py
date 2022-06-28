from os import environ
from app.main import app

if __name__ == "__main__":
	app.run(port=environ.get("PORT", 5000), host="0.0.0.0")
	