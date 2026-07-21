from fastapi import FastAPI
from app.router import router
from slowapi.middleware import SlowAPIMiddleware
from app.core.rate_limit import limiter


app = FastAPI(
      title="House Price Prediction API",
      version="1.0.0",
      description="REST API for predicting house prices using Linear Regression."
)


app.include_router(router)

app.state.limiter = limiter

app.add_middleware(SlowAPIMiddleware)