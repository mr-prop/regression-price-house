from joblib import load
from pathlib import Path
from fastapi import HTTPException

from app.core.Config import settings

MODEL_PATH=Path(settings.MODEL_PATH)

try:
    # load model
    model_load=load(MODEL_PATH)

except FileNotFoundError:
    #Error handling
    raise HTTPException(
        status_code=500,
        detail="Prediction failed."
    )