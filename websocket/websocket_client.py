import websockets
import asyncio

async def client():
    uri = 'ws://localhost:50089'
    async with websockets.connect(uri) as websocket:
        message = 'Привет, сервер!'
        print(f'Отправлено сообщение: {message}')
        await websocket.send(message)
        for _ in range(5):
            response = await websocket.recv()
            print(f'Ответ от сервера: {response}')

asyncio.run(client ())