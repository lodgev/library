## Gateway service

The gateway service is the main entry point for all client requests.
It routes traffic to individual microservices and handles JWT authentication.

### Environment variables (.env)
- `JWT_SECRET`: Secret key for JWT validation
- `USER_SERVICE_URL`: URL for user-service
- `BOOK_SERVICE_URL`: URL for book-service
- ...

### Run locally

```bash
cd services/gateway-service
uvicorn app.main:app --reload
```
### or via Docker Compose

```bash
docker-compose up gateway-service
```
### Requirements

```bash
pip install -r requirements.txt
```

### Structure

```bash
gateway-service/
├── app/
│   ├── main.py                 # entry point FastAPI
│   ├── routes/                 # HTTP routes
│   │   └── router.py           # endpoints
│   ├── services/               # requests to mictoservices
│   │   └── forward.py          
│   └── auth/                   # JWT-authentication
│       └── jwt.py              
├── .env                        
├── requirements.txt           
└── Dockerfile                 

```
