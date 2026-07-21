from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    # model
    MODEL_PATH:str="model/model_regression.joblib"
    # model version
    API_VERSION:str="v1"
    # name
    PROJECT_NAME:str="House Price Prediction API"
    # url
    ALLOWED_HOSTS:list[str]=[
        "http://localhost:8000"
    ]
    # confing model to .env
    class Config:
        env_file=".env"

settings=Settings()