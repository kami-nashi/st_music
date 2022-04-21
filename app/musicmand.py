import asyncio
import st_dbConf
import lib.logicMain as lm

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage


async def on_message(message: AbstractIncomingMessage) -> None:
    """
    on_message doesn't necessarily have to be defined as async.
    Here it is to show that it's possible.
    """

    url = message.body

    print("[mq] Received message %r" % message.delivery_tag)
    print("[mq] Message body is: %r" % message.body)
    lm.musicDownload(url.decode('utf-8'))
    #print("[mq] Discarding Message" % message.delivery_tag)


async def main() -> None:
    '''
    Handle the connection, channel, queue.
    Derived from st_dbConf settings
    '''

    mqConf = st_dbConf.stmq.musicman()

    connection = await connect("amqp://" + mqConf["user"] + ":" + mqConf["password"] + "@" + mqConf["host"])
    async with connection:
        # Creating a channel
        channel = await connection.channel()

        # Declaring queue
        queue = await channel.declare_queue(mqConf["queue"])

        # Start listening the queue
        await queue.consume(on_message, no_ack=True)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
