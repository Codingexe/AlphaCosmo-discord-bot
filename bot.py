import discord, asyncio, os, time
from discord.utils import get

class Initialisation:

    # On définit les variable globales
    global robot, prefix

    robot = discord.Client()
    prefix = '!'

class Main:

    # Si le robot est prêt, on l'indique à l'utilisateur
    @robot.event
    async def on_ready():
        print("\n The bot is ready to be use!")
        salon_generale = discord.Object(id='504242427327021070') # On récupère le salon générale du serveur

    @robot.event
    async def on_message(message):
        le_message = message.content
        channel    = message.channel

        cross = '❌'
        check = '✅'

        # GAME PARTY
        if le_message.startswith(prefix + "startGame \"") and le_message.endswith("\""):
            question = le_message[12:-1]
            await robot.delete_message(message)
            qa_embed = discord.Embed(title="QUESTION/ANSWER GAME", description="!startGame \"question\" for create a new game", color=0x00ff00)
            qa_embed.add_field(name=" ", value=' ', inline=False)

            qa_embed.add_field(name="Question: ", value=question, inline=False)
            qa_embed.add_field(name="Question of: ", value=message.author, inline=False)

            await robot.send_message(channel, embed=qa_embed)
        elif message.author == robot.user:
            await robot.add_reaction(message, check)
            await robot.add_reaction(message, cross)

        # MAKE TALK THE BOT
        if le_message.startswith(prefix + "say "):
            await robot.delete_message(message)
            await robot.send_message(channel, le_message[5:])

        # CLEAR COMMAND
        elif le_message.startswith(prefix + "clear "):
            msg_to_del = int(le_message[7:])
            deleted = await robot.purge_from(message.channel, limit=msg_to_del)

class Connexion:
    try:
        robot.run(process.env.BOT_TOKEN) # On démarre le robot grâce a sa clef d'accès, NE JAMAIS DIVULGUER
    except Exception as e:
        print("The robot can't connect, verify your internet connection")
