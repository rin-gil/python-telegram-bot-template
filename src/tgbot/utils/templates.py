"""
Module for rendering jinja2 templates used to display messages in the bot
Contains the RenderTemplate class, which performs template rendering, and template - object of the RenderTemplate class

Example of use:
    Importing an instance of the RenderTemplate class:
        from tgbot.utils.templates import template

    Create a handler in the handler module:
        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            await update.message.reply_text(
                text=await template.render(
                    template_name="start.jinja2", data={"user_name": update.message.from_user.first_name}
                )
            )

    ... and register it:
        start_handler: CommandHandler = CommandHandler(command="start", callback=start)

    in template "start.jinja2" specify:
        👋 Hello, {{ user_name }}!

    bot's output response to the /start command:
        👋 Hello, Alex!

More information about jinja2: https://jinja.palletsprojects.com/en/3.1.x/
"""

from jinja2 import Environment, FileSystemLoader, TemplateNotFound

from tgbot.config import TEMPLATES_DIR
from tgbot.utils.logger import logger


class RenderTemplate:
    """Returns the rendered template, based on the passed data"""

    def __init__(self, path_to_templates: str) -> None:
        """
        Initializing a class

        :param path_to_templates: path to the folder with templates
        :type path_to_templates: str
        """
        self._template_loader: FileSystemLoader = FileSystemLoader(searchpath=path_to_templates)
        self._env: Environment = Environment(loader=self._template_loader, enable_async=True)

    async def render(self, template_name: str, data: dict | None = None) -> str:
        """
        Returns the rendered template, based on the passed data

        :param template_name: template name
        :type template_name: str
        :param data: the data that will be passed to the template for display
        :type data: dict | None
        :return: rendered template as a string
        :rtype: str
        """
        if data is None:
            data = {}
        try:
            return await self._env.get_template(name=template_name).render_async(**data)
        except TemplateNotFound as exc:
            logger.error("Template %s for render not found: %s", template_name, repr(exc))
            return "❌ Answer template not found!"


template: RenderTemplate = RenderTemplate(path_to_templates=TEMPLATES_DIR)
