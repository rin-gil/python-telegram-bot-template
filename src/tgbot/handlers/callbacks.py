"""
In this module you can create functions that respond to user presses of buttons

Example:
    Create a function that will get some test data from the button and display it in the response message:
        async def test_call(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            data: str = update.callback_query.data
            await update.callback_query.message.reply_text(text=f"I got this data: {data}")
    Let's register a callback handler:
        test_call_handler: CallbackQueryHandler = CallbackQueryHandler(callback=some_call, pattern="some_test_data")

        some_test_data is the data from the button pressed by the user and can be used in the test_call function

Read more at: https://docs.python-telegram-bot.org/en/stable/telegram.callbackquery.html#callbackquery

Note:
    Handlers are imported into the __init__.py package handlers,
    where a tuple of HANDLERS is assembled for further registration in the application
"""
