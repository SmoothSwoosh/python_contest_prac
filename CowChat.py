import asyncio
from cowsay import list_cows, cowsay
import shlex


clients = {}

AVAILABLE_COWS = {cow for cow in list_cows()}
TAKEN_COWS = set()


async def chat(reader, writer):
    try:
        my_cowname = None
        my_queue = asyncio.Queue()
        send = asyncio.create_task(reader.readline())
        receive = asyncio.create_task(my_queue.get())
        while not reader.at_eof():
            done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
            for q in done:
                if q is send:
                    send = asyncio.create_task(reader.readline())

                    k = q.result().decode().strip()
                    message = shlex.split(k)
                    #print(f"GOT meeage {message}, {k}")
                    match message:
                        case ["cows"]:
                            await my_queue.put(f"{AVAILABLE_COWS}")
                            #print("ASKING FOR COWS")
                        case ["who"]:
                            await my_queue.put(f"{TAKEN_COWS}")
                        case ["login", cow_name] if my_cowname is None:
                            if cow_name in AVAILABLE_COWS:
                                AVAILABLE_COWS.remove(cow_name)
                                TAKEN_COWS.add(cow_name)
                                my_cowname = cow_name
                                clients[cow_name] = my_queue
                                await my_queue.put(f"You are registered as {cow_name}")
                            else:
                                await my_queue.put(f"COW is taken")
                        case ["say", cow_name, msg_text] if cow_name is not None:
                            if cow_name in TAKEN_COWS:
                                await clients[cow_name].put(cowsay(msg_text, cow=my_cowname))
                            else:
                                await my_queue.put("I don't know this cow")
                        case ["yield", msg_text] if my_cowname is not None:
                            for out in clients.values():
                                if out is not my_queue:
                                    await out.put(cowsay(msg_text, cow=my_cowname))
                        case ["GET_COWS"]:
                            await my_queue.put(str(list(AVAILABLE_COWS)))
                        case ["GET_COWS_USED"]:
                            await my_queue.put(str(list(TAKEN_COWS)))
                        case ["quit"]:
                            AVAILABLE_COWS.add(my_cowname)
                            TAKEN_COWS.remove(my_cowname)
                            clients.pop(my_cowname)
                            await my_queue.put(f"Good bye")
                            send.cancel()
                            receive.cancel()
                            writer.close()
                            await writer.wait_closed()
                            return
                        case _:
                            await my_queue.put("Maybe you need to register first")
                elif q is receive:
                    receive = asyncio.create_task(my_queue.get())
                    s = q.result()
                    writer.write(f"{s}\n".encode())
                    await writer.drain()
        send.cancel()
        receive.cancel()
        del clients[my_cowname]
        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(e)


async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 8080)
    async with server:
        await server.serve_forever()


asyncio.run(main())
