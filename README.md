Struct
```
fast_api/
├── app/
│   ├── api/              
│   │   └── v1/
│   │       ├── endpoints
│   │       │   └── coupon.py
│   │       │ 
│   │       └── routes.py
│   ├── core/
│   │   ├── config.py
│   │   ├── dependence.py
│   │   ├── response.py
│   │   └── database.py
│   ├── models/
│   │   └── coupon.py
│   ├── repositories/
│   │   └── coupon_repository.py
│   ├── schemas/
│   │   └── coupon.py
│   ├── services/
│   │   └── coupon_service.py
│   └── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

Migration:
```
# Create: 
alembic revision -m "create coupons table"

# Update: 
alembic upgrade head

# Downgrade: 
alembic downgrade -1
```
