"""
Evaluate CodeQL scan false positive with `py/unused-local-variable`.

`DummyTable` is an SQLAlchemy model definition. By its nature,
it just needs to be defined, and not necessarily *used*.

Synopsis::

    pip install pytest crate[sqlalchemy]
    docker run --rm -it --publish=4200:4200 crate:5.1.1
    pytest unused-local-variable.py
"""
from unittest.mock import MagicMock, patch

import pytest
import sqlalchemy as sa
from crate.client.cursor import Cursor
from crate.client.sqlalchemy.types import ObjectArray
from sqlalchemy.orm import declarative_base

fake_cursor = MagicMock(name="fake_cursor")
FakeCursor = MagicMock(name="FakeCursor", spec=Cursor)
FakeCursor.return_value = fake_cursor


class DbWrapper:
    def __init__(self):
        self.engine = sa.create_engine("crate://")
        self.Base = declarative_base(bind=self.engine)


@pytest.fixture
def db():
    return DbWrapper()


@patch("crate.client.connection.Cursor", FakeCursor)
def test_table_with_object_array(db):
    class DummyTable(db.Base):
        __tablename__ = "t"
        pk = sa.Column(sa.String, primary_key=True)
        tags = sa.Column(ObjectArray)

    db.Base.metadata.create_all()
    fake_cursor.execute.assert_called_with(
        (
            "\nCREATE TABLE t (\n\t"
            "pk STRING, \n\t"
            "tags ARRAY(OBJECT), \n\t"
            "PRIMARY KEY (pk)\n)\n\n"
        ),
        (),
    )
