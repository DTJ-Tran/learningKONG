✅ README.md

# 🚀 API Gateway with Kong and Flask (Docker-based)

This project demonstrates how to use **Kong API Gateway** to manage and route requests to multiple **Flask-based services** using **Docker Compose**.

---

## 🧱 Project Structure

<pre>
```plaintext
learningKONG/
├── flask-api/         # Backend Flask app (API)
│   └── app.py
├── flask-ui/          # Frontend UI app (Form input)
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```
</pre>


## 📦 Setup Instructions

### 1. Build & Start Services

```bash
docker-compose build
docker-compose up -d

2. Bootstrap Kong (Run ONCE after DB is created)

docker-compose run --rm kong kong migrations bootstrap


⸻

🔌 Register Services with Kong

Register Backend API (flask-api)

curl -i -X POST http://localhost:8001/services/ \
  --data name=flask-api \
  --data url=http://flask-api:5001/

curl -i -X POST http://localhost:8001/services/flask-api/routes \
  --data 'paths[]=/flask'

Register Frontend UI (flask-ui)

curl -i -X POST http://localhost:8001/services/ \
  --data name=flask-ui \
  --data url=http://flask-ui:5002/

curl -i -X POST http://localhost:8001/services/flask-ui/routes \
  --data 'paths[]=/ui'


⸻

🌐 Access the Services via Kong
	•	http://localhost:8000/flask → Backend API
	•	http://localhost:8000/ui → Text Input UI

⸻

⚠️ Important Notes on Docker Volumes
	•	If you run docker-compose down -v, your Kong database (PostgreSQL) will be deleted.
	•	This means you’ll need to re-bootstrap Kong and re-register services.

✅ Instead, just use:

docker-compose down    # Keeps volumes safe

🔁 Then restart with:

docker-compose up -d


⸻

🧼 Resetting (If Needed)

docker volume rm learningkong_kong_data
docker-compose up -d
docker-compose run --rm kong kong migrations bootstrap


⸻

🛠️ Useful Commands

List registered services:

curl http://localhost:8001/services

List routes:

curl http://localhost:8001/routes


⸻

📚 References
	•	Kong Docs
	•	Flask Docs
	•	Docker Compose Docs

