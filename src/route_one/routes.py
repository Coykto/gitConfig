from src.route_one.schemas import SomeInput, SomeOutput


async def supporting_method(num: int):
    return num * num


async def run(method_input: SomeInput) -> SomeOutput:
    result = await supporting_method(method_input.num)
    return SomeOutput(result=result)

