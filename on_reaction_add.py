import logging

import discord

from modis import main
from . import _data, ui_embed

logger = logging.getLogger(__name__)


async def on_reaction_add(reaction, user):
    # Simplify message info
    msgobj = reaction.message
    emoji = reaction.emoji

    guild = msgobj.guild
    author = msgobj.author
    channel = msgobj.channel
    content = msgobj.content

    # Commands
    if emoji == '':
        # now = "now" in aux
        await channel.send(embed=ui_embed.vote_ui())
    if emoji == '':
        pass
