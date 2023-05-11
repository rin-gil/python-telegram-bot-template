# python-telegram-bot-template

---

<p align="center">
    <a href="https://www.python.org/downloads/release/python-3110/">
            <img src="https://img.shields.io/badge/python-v3.11-informational" alt="python version">
    </a>
    <a href="https://pypi.org/project/python-telegram-bot/20.3/">
            <img src="https://img.shields.io/badge/python_telegram_bot-v20.3-informational" alt="python-telegram-bot version">
    </a>
    <a href="https://pypi.org/project/aiolimiter/1.1.0/">
            <img src="https://img.shields.io/badge/aiolimiter-v1.1.0-informational" alt="aiolimiter version">
    </a>
    <a href="https://pypi.org/project/Jinja2/3.1.2/">
            <img src="https://img.shields.io/badge/Jinja2-v3.1.2-informational" alt="Jinja2 version">
    </a>
    <a href="https://pypi.org/project/environs/9.5.0/">
            <img src="https://img.shields.io/badge/environs-v9.5.0-informational" alt="environs version">
    </a>
    <a href="https://github.com/rin-gil/python-telegram-bot-template/blob/master/LICENCE">
        <img src="https://img.shields.io/badge/licence-MIT-success" alt="MIT licence">
    </a>
</p>
<p align="center">
    <a href="https://github.com/psf/black">
            <img src="https://img.shields.io/badge/code%20style-black-black.svg" alt="Code style: black">
    </a>
    <a href="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/codeql.yml">
            <img src="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/codeql.yml/badge.svg" alt="CodeQL">
    </a>
    <a href="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/dependency-review.yml">
            <img src="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/dependency-review.yml/badge.svg" alt="Dependency Review">
    </a>
    <a href="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/mypy.yml">
            <img src="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/mypy.yml/badge.svg" alt="MyPy">
    </a>
    <a href="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/pylint.yml">
            <img src="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/pylint.yml/badge.svg" alt="Pylint">
    </a>
    <a href="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/unittests.yml">
            <img src="https://github.com/rin-gil/python-telegram-bot-template/actions/workflows/unittests.yml/badge.svg" alt="Unit Tests">
    </a>
</p>

---

#### This template can be used for telegram bots written using the [python-telegram-bot](https://python-telegram-bot.org) library.

#### Detailed materials on creating bots can be found in the [documentation](https://docs.python-telegram-bot.org/en/stable/) and [wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki).

### Template structure:

```
src/
├── tgbot/  
│   ├── assets/
│   ├── handlers/
│   ├── services/
│   ├── templates/
│   ├── utils/
│   ├── __init__.py
│   └── config.py
├──.env.example
└── bot.py
```

### Description:

* `tgbot/` - the root package, which contains the other sub-packages and files necessary for the bot's operation
* `assets/` - resources that can be used in the bot, such as images, logos
* `handlers/` - handlers that respond to the actions of bot users
* `services/` - the business logic of the bot
* `templates/` - to avoid writing text in handlers, the message templates are placed in a separate module
* `utils/` - other support modules
* `config.py` - configuration file
* `.env.example` - file with environment variables, you need to rename it to `.env` and insert your bot's token into it
* `bot.py` - entry point for the bot, performs preparatory operations and launches the bot

A more detailed description and documentation of all bot functions are in the template.

### Developers

* [Ringil](https://github.com/rin-gil)

### License

YouTubeMusicDownloadBot is licensed under [MIT](https://github.com/rin-gil/YoutubeMusicDownloadBot/blob/master/LICENCE)