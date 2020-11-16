import websockets
import asyncio

# --Identify the client
async def identify(websocket, path):
    id = await websocket.recv()
    #Process the id
    print("Processed id")
    await websocket.send("Hello")

server = websockets.serve(identify, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
