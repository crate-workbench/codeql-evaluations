"""
Evaluate CodeQL scan false positive with `py/call-to-non-callable`.

Synopsis::

    pytest call-to-non-callable.py
"""


class Command(object):
    def __call__(self, cmd, *args, **kwargs):
        pass


class FooBarCommand(Command):
    def __call__(self, cmd, *args, **kwargs):
        return f"{cmd}: foobar"


def test_object_callable():
    foobar = FooBarCommand()
    result = foobar("hello")
    assert result == "hello: foobar"
