from src.route_two.schemas import InputTwo, OutputTwo


async def supporting_method(s: str) -> str:
    return s * 4


async def run(string_input: InputTwo) -> OutputTwo:
    res = await supporting_method(string_input.s)
    return OutputTwo(result=res)

