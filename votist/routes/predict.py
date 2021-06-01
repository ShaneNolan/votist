from fastapi import APIRouter, Depends

from votist.schemas.payment import PaymentSchema
from votist.schemas.prediction import PredictionSchema
from votist.services.fraud_model import FraudModel, get_fraud_model

predict_router = APIRouter()


@predict_router.post(
    '/predict',
    response_model=PredictionSchema,
    name='predict',
)
async def predict(
    payment: PaymentSchema,
    fraud_model: FraudModel = Depends(get_fraud_model),  # noqa: B008, WPS404
) -> PredictionSchema:
    return PredictionSchema(
        fraudulent=fraud_model.score(
            payment.to_model_list(),
        ),
    )
