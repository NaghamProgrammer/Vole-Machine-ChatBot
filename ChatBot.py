class VoleBot:
    def __init__(self):
        # Define the instructions dictionary with explanations
        self.instructions = {
            "b": "JUMP to the location in the memory cell at address {address} if the bit pattern in register {reg} is equal to the bit pattern in register 0. Otherwise, continue with the normal sequence of execution.",
            "1": "LOAD the value from memory cell at address {address} into register {reg}.",
            "2": "LOAD the immediate value {value} into register {reg}.",
            "3": "STORE the value from register {reg} into memory cell at address {address}.",
            "4": "MOVE the value from register {reg1} to register {reg2}.",
            "5": "ADD the values in registers {reg1} and {reg2}, store the result in register {reg3}.",
            "6": "ADD floating-point numbers in registers {reg1} and {reg2}, store the result in register {reg3}.",
            "7": "OR bitwise operation between values in registers {reg1} and {reg2}, store the result in register {reg3}.",
            "8": "AND bitwise operation between values in registers {reg1} and {reg2}, store the result in register {reg3}.",
            "9": "XOR bitwise operation between values in registers {reg1} and {reg2}, store the result in register {reg3}.",
            "a": "ROTATE right by {count} positions the value in register {reg}.",
            "c": "HALT the machine.",
            "d": "JUMP to the location in memory at address {address} if the value in register {reg} is greater than the value in register 0."
        }

    def explain_instruction(self, user_input):
        user_input = user_input.lower()  # Convert to lowercase
        instr = user_input[0]  # The instruction code
        address = user_input[2:]  # Address or value part (for 2 hex digits)
        
        # Check if instruction exists in dictionary
        if instr in self.instructions:
            explanation = self.instructions[instr]

            # Substitute placeholders based on the type of instruction
            if instr == "b" or instr == "d":
                reg = user_input[1]
                return explanation.format(address=address, reg=reg)
            elif instr == "1" or instr == "3":
                reg = user_input[1]
                return explanation.format(address=address, reg=reg)
            elif instr == "2":
                reg = user_input[1]
                value = address
                return explanation.format(value=value, reg=reg)
            elif instr == "4":
                reg1 = user_input[1]
                reg2 = user_input[2]
                return explanation.format(reg1=reg1, reg2=reg2)
            elif instr in ["5", "6", "7", "8", "9"]:
                reg1 = user_input[1]
                reg2 = user_input[2]
                reg3 = user_input[3]
                return explanation.format(reg1=reg1, reg2=reg2, reg3=reg3)
            elif instr == "a":
                reg = user_input[1]
                count = int(address, 16)  # Rotate count as a number
                return explanation.format(reg=reg, count=count)
            elif instr == "c":
                return explanation
            else:
                return "Unknown instruction format."
        else:
            return "Instruction not recognized. Please check your input."

# Main loop to interact with the user
if __name__ == "__main__":
    bot = VoleBot()
    print("VoleBot: Hello! Enter a Vole machine instruction to learn what it does (e.g., 'b3ff'). Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("VoleBot: Goodbye!")
            break
        explanation = bot.explain_instruction(user_input)
        print("VoleBot:", explanation)
