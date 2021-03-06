"""Thinkific tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers


from tap_thinkific.streams import (
    GroupsStream,
    CoursesStream,
    EnrollmentsStream,
    ProductsStream,
    UsersStream,
    GroupsUsersStream
)

STREAM_TYPES = [
    GroupsStream,
    CoursesStream,
    EnrollmentsStream,
    ProductsStream,
    UsersStream,
    GroupsUsersStream
]


class TapThinkific(Tap):

    name = "tap-thinkific"

    config_jsonschema = th.PropertiesList(
        th.Property("auth_token", th.StringType, required=True),
        th.Property("subdomain", th.StringType, required=True),
        th.Property("api_url", th.StringType, required=True),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [
            stream_class(tap=self)
            for stream_class in STREAM_TYPES
        ]
