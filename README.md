## SOCKS proxy client for aiohttp 3.0+
**DEPRECATED: please use new [aiohttp-socks](https://github.com/romis2012/aiohttp-socks) package**

It`s a fork of [aiosocks](https://github.com/nibrag/aiosocks) with minor fixes for aiohttp 3.0+ compatibility

## Requirements
- Python >= 3.5.3
- aiohttp >= 3.0

## Installation
```
pip install aiosocksy
```

## Usage

```python
import asyncio
import aiohttp
from aiosocksy import Socks5Auth
from aiosocksy.connector import ProxyConnector, ProxyClientRequest


async def fetch(url):
    auth = Socks5Auth(login='...', password='...')
    connector = ProxyConnector()
    socks = 'socks5://127.0.0.1:1080'
    async with aiohttp.ClientSession(connector=connector, request_class=ProxyClientRequest) as session:
        async with session.get(url, proxy=socks, proxy_auth=auth) as response:
            print(await response.text())


loop = asyncio.get_event_loop()
loop.run_until_complete(fetch('https://www.google.com/'))
```

see [aiosocks](https://github.com/nibrag/aiosocks) for more examples
