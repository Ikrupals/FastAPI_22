import logging

from fastapi import APIRouter, Depends, Request, status, Response, FastAPI
from psycopg.rows import dict_row

from api.account.model import Account_Types, Accounts, \
    MasterAccountCategories, MasterClaims, MasterMicroServices, \
        MasterPolicies, RoleWisePoliciesAndPermissions, Roles, UserAccounts

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

router = APIRouter()
app = FastAPI()

@router.post('/account_types', status_code=status.HTTP_200_OK,
             name="Get all accounts types", response_model=list[Account_Types])
async def get_accounts_types(request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM accounts.account_types"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.get('/account_type/{app_short_code}', status_code=status.HTTP_200_OK,
            name="Get account type by app_short_code", response_model=list[Account_Types])
async def get_account_type_by_app_short_code(app_short_code, request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT * 
                FROM accounts.account_types WHERE app_short_code = %s""", (app_short_code,)
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.post('/accounts', status_code=status.HTTP_200_OK,
             name="Get all accounts", response_model=list[Accounts])
async def get_all_accounts(request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM accounts.accounts"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.get('/account/{app_short_code}', status_code=status.HTTP_200_OK,
            name="Get account by app_short_code", response_model=list[Accounts])
async def get_account_by_app_short_code(app_short_code, request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT * 
                FROM accounts.accounts WHERE app_short_code = %s""", (app_short_code,)
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.post('/master_account_categories', status_code=status.HTTP_200_OK,
             name="Get all master account categories", response_model=list[MasterAccountCategories])
async def get_master_account_categories(request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM accounts.master_account_categories"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.post('/master_claims', status_code=status.HTTP_200_OK,
             name="Get all master claims", response_model=list[MasterClaims])
async def get_master_claims(request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM accounts.master_claims"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.post('/master_microservices', status_code=status.HTTP_200_OK,
             name="Get all master microservices", response_model=list[MasterMicroServices])
async def get_master_microservices(request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM accounts.master_microservices"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.post('/master_policies', status_code=status.HTTP_200_OK,
             name="Get all master policies", response_model=list[MasterPolicies])
async def get_master_policies(request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM accounts.master_policies"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.post('/role_wise_policies_and_permissions', status_code=status.HTTP_200_OK,
             name="Get all role wise policies and permissions",
             response_model=list[RoleWisePoliciesAndPermissions])
async def get_all_role_wise_policies_and_permissions(request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM accounts.role_wise_policies_and_permissions"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.get('/role_wise_policies_and_permissions/{app_short_code}',
            status_code=status.HTTP_200_OK,
            name="Get role wise policies and permissions by app_short_code",
            response_model=list[RoleWisePoliciesAndPermissions])
async def get_role_wise_policies_and_permissions_by_app_short_code(app_short_code, request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT * 
                FROM accounts.role_wise_policies_and_permissions WHERE app_short_code = %s""", (app_short_code,)
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.post('/roles', status_code=status.HTTP_200_OK, name="Get all roles",
             response_model=list[Roles])
async def get_all_roles(request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM accounts.roles"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.get('/role/{app_short_code}', status_code=status.HTTP_200_OK,
            name="Get role by app_short_code", response_model=list[Roles])
async def get_role_by_app_short_code(app_short_code, request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT * 
                FROM accounts.roles WHERE app_short_code = %s""", (app_short_code,)
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.post('/user_accounts', status_code=status.HTTP_200_OK,
             name="Get all user accounts", response_model=list[UserAccounts])
async def get_all_user_accounts(request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM accounts.user_accounts"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

@router.get('/user_account/{app_short_code}', status_code=status.HTTP_200_OK,
            name="Get user account by app_short_code", response_model=list[UserAccounts])
async def get_user_account_by_app_short_code(app_short_code, request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT * 
                FROM accounts.user_accounts WHERE app_short_code = %s""", (app_short_code,)
            )
            results = await cur.fetchall()
            logger.info(results)
            return results

# @router.post('/account', status_code=status.HTTP_201_CREATED, name="create an account")
# async def create_account(account: Account, request: Request):
#     async with request.app.async_pool.psyco_async_pool.connection() as conn:
#         async with conn.cursor(row_factory=dict_row) as cur:
#             await cur.execute("""
#                 INSERT INTO
#                 account.accounts (id, name, parent_account_id, category, type, adress_line_1, adress_line_2, contact_name, contact_email, contact_phone)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (account.id, account.name, account.parent_account_id, account.category, account.type, account.adress_line_1, account.adress_line_2, account.contact_name, account.contact_email, account.contact_phone)
#             )

