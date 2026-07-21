from fastapi import APIRouter , status , Request
from app.core.rate_limit import limiter
from app.schemas.request import HouseFeatures
from app.services.prediction_service import PredictionService

# Making a router
router = APIRouter(
    prefix="/api/v1/predict",
    tags=["Prediction"]
)
dt:list[dict] = []

@router.post("/" , status_code=status.HTTP_200_OK)
@limiter.limit("20/minute")
def pred(request : Request , input:HouseFeatures):
    """
    Predict house price using trained model.
    """

    service = PredictionService()
    service_result = service.predict(input)

    item = input.model_dump()
    item["prediction"] = service_result

    dt.append(item)

    return {
        "status" : "success",
        "prediction" : service_result
    }


@router.get("/get" , status_code=status.HTTP_200_OK)
def get_data():
    return {
        "count":len(dt),
        "data":dt
    }


