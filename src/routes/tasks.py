import datetime
import json
from http import HTTPStatus
from typing import List

import pytz
import redis
from fastapi import APIRouter

from src.schemas import TaskSchema, TaskTimeSchema

router = APIRouter(prefix='/Tasks', tags=['Tasks'])
client = redis.StrictRedis(host='localhost', port=6379, db=0)
sp_timezone = pytz.timezone('America/Sao_Paulo')


@router.post('/', status_code=HTTPStatus.CREATED, response_model=TaskSchema)
def create_task(task: TaskSchema):
    current_time = datetime.datetime.now(sp_timezone)
    time_remaining = int(
        (
            task.date_limit.replace(tzinfo=sp_timezone) - current_time
        ).total_seconds()
    )
    if time_remaining > 0:
        task_data = json.dumps({
            'Name': task.name,
            'Time Remaining': time_remaining,
        })
        client.setex(task.name, time_remaining, task_data)
        return task


@router.get(
    '/', status_code=HTTPStatus.OK, response_model=List[TaskTimeSchema]
)
def read_tasks():
    tasks = []
    for key in client.keys('*'):
        task_data = client.get(key)
        if task_data:
            ttl = client.ttl(key)
            tasks.append(
                TaskTimeSchema(name=key.decode('utf-8'), time_remaining=ttl)
            )
    return tasks


@router.delete('/{task_name}', status_code=HTTPStatus.OK)
def delete_task(task_name: str):
    client.delete(task_name)
    return {'message': 'Task deleted successfully', 'task name': task_name}
