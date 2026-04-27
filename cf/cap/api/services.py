from dataclasses import dataclass

from models import ApiDTO


@dataclass(frozen=True)
class Result:
    hello: str


def toService(value: str) -> Result:
    return ApiDTO(
        value=value,
    ).toJson()
