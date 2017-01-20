#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-

import orm
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time

from datetime import datetime
from aiohttp import web
from models import User, Blog, Comment

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html', charset='UTF-8')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), 'localhost', 9000)
    logging.info('server started at http://139.162.86.58:9000...')
    return srv

async def test():
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

    u = User(id='001484730194897cceb54da6cb6474b8122381e0cebd571000', name='Jared Han', email='hanjiawei@outlook.com', passwd='1234567890', image='about:blank', admin=False)

    await u.update()
    logging.info('test ok')

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
