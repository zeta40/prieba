from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey  {}
Bienvenido 😁

Yo hago sticker y fotos
1) Sí me envías un esticker crearé una imagen
2) Sí me envías una imagen crearé un esticker

🤗🤗🤗🤗🤗
By @nautaii
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨  OPINAR :) ✨", url="https://t.me/stikerino")],
        [InlineKeyboardButton(text="🏠 VOLVER ATRÁS 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ OPINAR :) ✨", url="https://t.me/nautaii")
        ],
        [
            InlineKeyboardButton("AYUDA😋", callback_data="help"),
            InlineKeyboardButton("🎪 INFORMACIO N 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ DESAROLLADOR ♥", url="https://t.me/nautaii")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/stikerino")],
    ]

    # Help Message
    HELP = """
💚COMO USARME💚

1) Envíame un sticker para crear una imagen
2) Envíame una imagen para crear un sticker

Nota : VAMOS A TROLEAR😂

BOT CREADO POR @nautaii.
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