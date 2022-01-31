from ..utils import Abot


@Abot(pattern="^/setfooter ?(.*)")
async def set_footer_channel____(e):
    if not e.is_channel or e.is_group:
        return await e.reply("This command is made to be used in channels, not in pm!")
    print("x")
