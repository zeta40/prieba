from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use this bot to convert
1) Sticker to Image
2) Image to Sticker

Send Multiple images or stickers and it will work the same

By @nautaii
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨  Bot Status and More Bots ✨", url="https://t.me/chditoo")],
        [InlineKeyboardButton(text="🏠 VOLVER ATRÁS 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/nautaii")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ DESAROLLADOR ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/chditoo")],
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

1) Send Sticker to get Image
2) Send Image to get Sticker

Note : You can send any amount of images or stickers or both together at once and it will work with same speed and accuracy.

More features in development. Keep track by joining @nautaii.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @nautaii

Source Code : [@nautai)

Framework : [Pyrogram](😌)

Language : [Python]

Developer : @nautaii
    """