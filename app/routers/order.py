import logging
import os
from datetime import datetime
from http import HTTPStatus
from typing import Dict

from fastapi import APIRouter

from app.routers.storage_module import Storage

logger = logging.getLogger(__file__)
router = APIRouter(tags=['income'])


storage = Storage(os.getenv('STORAGE_HOST', 'http://localhost:8001'))


@router.post('/order', status_code=HTTPStatus.OK)
async def order_call(order: str) -> Dict[str, str]:
    logger.info(f'Incoming order: {order}')
    filename = f'order-{datetime.utcnow().strftime("%Y-%m-%d--%H-%M-%S--%f")}--UTC.txt'
    storage.create_file(filename, order)
    logger.info(f'Stored file: {filename}')
    return {'Received order': order}
