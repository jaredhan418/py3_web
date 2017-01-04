import asyncio, logging

import aiomysql

@asyncio.coroutine
def creat_pool(loop,**kw):
    logging.info('creat database connection pool...')
