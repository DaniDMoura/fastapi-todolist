from http import HTTPStatus

from fastapi import FastAPI

from src.routes import tasks

app = FastAPI()
app.include_router(tasks.router)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {
        'message': 'Visit /docs for interactive API documentation provided by Swagger UI.'
    }
