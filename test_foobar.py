from foobar import FooBarCommand


def test_foobar():
    foobar = FooBarCommand()
    result = foobar("hello")
    assert result == "hello: foobar"
