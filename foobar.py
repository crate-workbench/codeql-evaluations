class Command(object):

    def __call__(self, cmd, *args, **kwargs):
        pass


class FooBarCommand(Command):

    def __call__(self, cmd, *args, **kwargs):
        return f"{cmd}: foobar"
