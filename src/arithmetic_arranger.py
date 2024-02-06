def arithmetic_arranger(operations, show_result=True):
    if len(operations) > 5:
        return "Error: Too many problems."

    problems = ""
    for operation in operations:
        operands = operation.split()
        if len(operands[0]) > 4 or len(operands[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operands[1] not in ("+", "-"):
            return "Error: Operator must be '+' or '-'"
        if not operands[0].isdigit() or not operands[2].isdigit():
            return "Error: Numbers must only contains digits."

        width = max(len(operands[0]), len(operands[2])) + 2
        problems += f"{operands[0]:>{width}}\n"
        problems += f"{operands[1]} {operands[2]:>{width - 2}}\n"
        problems += f"{'-' * width}\n"

        if show_result:
            operators = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
            }
            result = operators[operands[1]](int(operands[0]), int(operands[2]))
            problems += f"{result:>{width}}\n"

    return problems.rstrip()


sample_operation = ["5 + 10", "2 - 1", "1324 + 1453"]
sample = arithmetic_arranger(sample_operation, True)
print(sample)
