import logging

from fastapi import APIRouter, Depends, Request, status, Response, FastAPI
from psycopg.rows import dict_row

from api.application.model import Application


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

router = APIRouter()
app = FastAPI()


@router.post('/applications', status_code=status.HTTP_200_OK,
             name="Get all applications", response_model=list[Application])
async def get_applications(
        request: Request                 
    ):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM applications.applications"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.get('/application/{short_code}', status_code=status.HTTP_200_OK,
            name="Get application by short_code", response_model=list[Application])
async def get_application_by_short_code(short_code, request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT * 
                FROM applications.applications WHERE short_code = %s""", (short_code,)
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

