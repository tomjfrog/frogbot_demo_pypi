import code

# Value supplied by user
user_input = input("print('pwned')")
console = code.InteractiveConsole()
# Vulnerable
console.push(user_input)


# Value supplied by user
user_input = input("print('pwned')")
interpreter = code.InteractiveInterpreter()
# Vulnerable
interpreter.runcode(code.compile_command(user_input))
interpreter.runcode(user_input)
