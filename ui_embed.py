"""UI Embed generator for music module"""

import logging

from modis.tools import embed

from . import _data

logger = logging.getLogger(__name__)


def vote_ui(channel, options):
    """
    Creates an embed UI for the topic update

    Args:
        channel (discord.Channel): The Discord channel to bind the embed to.
        options (dict): All the votable options with keys as the option and values as the number of votes the option has.

    Returns:
        gui (embed.UI): The created embed
    """

    # TODO parse [options] to create [message]

    # Create embed UI object
    gui = embed.UI(
            channel,
            "Ballot",
            message,
            modulename="decide",
            colour=_data.MODULECOLOUR_INFO
    )

    return gui
