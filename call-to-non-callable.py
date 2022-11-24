"""
Evaluate CodeQL scan false positive with `py/call-to-non-callable`.

Synopsis::

    pytest call-to-non-callable.py
"""
import functools


def noargs_command(func):
    @functools.wraps(func)
    def wrapper(self, cmd, *args, **kwargs):
        if len(args):
            cmd.logger.critical('Command does not take any arguments.')
            return
        return func(self, cmd, *args, **kwargs)
    return wrapper


class Command(object):
    def __call__(self, cmd, *args, **kwargs):
        pass


class FooBarCommand(Command):

    @noargs_command
    def __call__(self, cmd, *args, **kwargs):
        return f"{cmd}: foobar"


def test_object_callable():
    foobar = FooBarCommand()
    result = foobar("hello")
    assert result == "hello: foobar"
