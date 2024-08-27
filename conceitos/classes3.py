import inspect
from dataclasses import dataclass, field
from pprint import pprint


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str = ""
    replies: list[int] = field(default_factory=list, compare=True, hash=False, repr=False)


def main():
    comment = Comment(1, "I just subscribed!")
    print(comment)
    # print(astuple(comment))
    # print(asdict(comment))


if __name__ == '__main__':
    main()
