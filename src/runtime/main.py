from typing import Literal


type InputSegments = Literal["numbers", "names", "instructions"]
type Input = dict[InputSegments, str]


class Interpreter:
    def __init__(self) -> None:
        self.stack = []
        self.environment = {}

    def _STORE_NAME(self, name) -> None:
        val = self.stack.pop()
        self.environment[name] = val

    def _LOAD_NAME(self, name) -> None:
        self.stack.append(self.environment[name])

    def _LOAD_VALUE(self, number) -> None:
        self.stack.append(number)

    def _PRINT_ANSWER(self) -> None:
        print(self.stack.pop())

    def _ADD_TWO_NUMBERS(self) -> None:
        self.stack.append(self.stack.pop() + self.stack.pop())

    def parse_argument(self, instr, argument, input):
        numbers = ["_LOAD_VALUE"]
        names = ["_LOAD_NAME", "_STORE_NAME"]

        if instr in numbers:
            argument = input["numbers"][argument]
        elif instr in names:
            argument = input["names"][argument]

        return argument

    def parse(string: str): ...

    def execute(self, input: Input):
        instructions = input["instructions"]

        for step in instructions:
            instr, arg = step
            arg = self.parse_argument(instr, arg, input)
            bytecode_method = getattr(self, instr)
            if arg is None:
                bytecode_method()
            else:
                bytecode_method(arg)


def parser_string(string: str) -> Input: ...


if __name__ == "__main__":
    Interpreter().execute("7 + 5")
