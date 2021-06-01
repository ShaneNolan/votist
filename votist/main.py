from fastapi import FastAPI

from votist.routes.predict import predict_router


def get_app() -> FastAPI:
    fast_app = FastAPI(title='VOTIST', version='1.0', debug=True)
    fast_app.include_router(predict_router, prefix='/api/v1')

    return fast_app


app = get_app()
