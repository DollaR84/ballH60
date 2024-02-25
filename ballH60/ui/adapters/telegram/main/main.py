from .handlers import CallbackHandlers, CommandHandlers, MessageHandlers

from .about import AboutDialog


class Main:

    @classmethod
    def register(cls, **kwargs):
        AboutDialog.register(**kwargs)

        CallbackHandlers.register(**kwargs)
        CommandHandlers.register(**kwargs)
        MessageHandlers.register(**kwargs)
