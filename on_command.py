import logging

import discord

from modis import main
from . import _data, ui_embed

logger = logging.getLogger(__name__)


async def on_command(root, aux, query, msgobj):
    # Simplify message info
    guild = msgobj.guild
    author = msgobj.author
    channel = msgobj.channel
    content = msgobj.content

    logger.info("Root: {}, Aux: {}, Query: {}".format(root, aux, query))

    # Commands
    if root == 'vote':
        # now = "now" in aux
        await channel.send(embed=ui_embed.vote_ui())
    if root == 'choose':
        pass
