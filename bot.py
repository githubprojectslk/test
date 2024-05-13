from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls import idle
from pytgcalls.types import MediaStream
from pytgcalls import PyTgCalls, filters
from pytgcalls.types import Update
from pytgcalls.types import MediaStream,StreamVideoEnded
from pytgcalls.types import MediaStream
from pytgcalls.types import VideoQuality,AudioQuality

bot = Client('test',3413890,'4d309f9bb03ed141f5528b32f7866ad3')
p='n'

chat_id = -1002039534112
app = PyTgCalls(bot)
app.start()
app.play(
    chat_id,
    MediaStream(
        'http://103.151.60.214:7444/1102/video.m3u8'
    )
)
idle()


# @app.on_update(filters.stream_end)
# async def my_handler(client: PyTgCalls, update: Update):
#     global p
#     if p =='y':return
#     if isinstance(update, StreamVideoEnded):
#         await app.play(-1002039534112,stream=MediaStream('http://mag.trexlive.me:80/Michael88/Michael88/1114581',))







bot.run()

