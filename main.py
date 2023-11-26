import os
from dotenv import load_dotenv

import discord

from pydactyl import PterodactylClient

# .envファイルの内容を読み込見込む
load_dotenv()

# Pterodactylを読み込み
api = PterodactylClient(os.environ["DOMAIN"], os.environ["API"])

# UUIDを読み込み
serveruuid = os.environ["SERVERUUID"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# ログインしたとき
@client.event
async def on_ready():
    print(f"{client.user} としてログインしました")


# メッセージ反応
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # サーバー起動
    if message.content.startswith("$サーバーを起動して"):
        api.client.servers.send_power_action(serveruuid, "start")
        await message.channel.send("サーバーを起動しました")

    # サーバー停止
    if message.content.startswith("$サーバーを停止して"):
        api.client.servers.send_power_action(serveruuid, "stop")
        await message.channel.send("サーバーを停止しました")

    # サーバー再起動
    if message.content.startswith("$サーバーを再起動して"):
        api.client.servers.send_power_action(serveruuid, "restart")
        await message.channel.send("サーバーを再起動しました")


# os.environを用いて環境変数を表示させます
client.run(os.environ["DISTOKEN"])
