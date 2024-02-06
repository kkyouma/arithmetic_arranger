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


sample_operation = ["5 + 10", "2 - 1"]
arithmetic_arranger(sample_operation)
