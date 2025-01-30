import asyncio
import httpx
from django.http import HttpResponse
from time import sleep

async def http_call_async(): #async function
    for num in range(1,6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

def http_call_sync(): #sync function
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org")
    print(r)

async def async_view(request): #função assincrona utilizando event loop
    asyncio.create_task(http_call_async())
    return HttpResponse("Esta é uma requisição Non-blocking")

def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking requisição aqui!!")