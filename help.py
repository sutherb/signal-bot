

def helpScreen ():
    helpMessage = ("BOT COMMAND HELP\n\n"
        "PRICEBOT\n"
        "Example: /p btc\n"
        "\n"
        "CHARTBOT\n"
        "Examples: /c weth\n"
        " With range: /c btc month\n"
        " Range shortcut: /c btc 2w\n"
        "Ranges (default is month):\n"
        "ma(x), (y)ear, (h)alfyear,\n"
        " (q)uarter, (m)onth,\n"
        " (2w)eek,(w)eek, (d)ay\n\n"
        "Misc. Commands:\n"
        "Market Data: /cap\n"
        "ETH/BTC Dominance: /ethbtc\n"
        "Refresh coin list: /refresh\n"
        "This helpful screen! /?\n"

    )

    print(helpMessage)
    return helpMessage