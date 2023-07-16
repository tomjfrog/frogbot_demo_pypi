import asyncio
import subprocess
import sys
import os
from flask import request

# Vulnerable
user_input1 = request.args.get("/foo/bar") # value supplied by user
os.spawnlpe(os.P_WAIT, user_input1, ["-a"], os.environ)

# Vulnerable
user_input2 = request.args.get("cat /etc/passwd") # value supplied by user
os.spawnve(os.P_WAIT, "/bin/bash", ["-c", user_input2], os.environ)

# Vulnerable
user_input3 = request.args.get("foo && cat /etc/passwd") # value supplied by user
os.system("grep -R {} .".format(user_input3))

# Vulnerable
user_input4 = request.args.get("foo && cat /etc/passwd") # value supplied by user
os.popen("ls -l " + user_input4)


# Vulnerable
user_input5 = request.args.get("foo && cat /etc/passwd") # value supplied by user
subprocess.call("grep -R {} .".format(user_input5), shell=True)

# Vulnerable
user_input6 = request.args.get("cat /etc/passwd") # value supplied by user
subprocess.run(["bash", "-c", user_input6], shell=True)

# Not vulnerable
user_input7 = request.args.get("cat /etc/passwd") # value supplied by user
subprocess.Popen(['ls', '-l', user_input7])

# Not vulnerable
user_input8 = request.args.get("cat /etc/passwd") # value supplied by user
subprocess.check_output('ls -l dir/')


# prints home directory
user_input9 = request.args.get("cat /etc/passwd") # value supplied by user
subprocess.call('echo $HOME', shell=True)

# throws an error
user_input10 = request.args.get("cat /etc/passwd") # value supplied by user
subprocess.call('echo $HOME', shell=False)


# Vulnerable
user_input11 = request.args.get("/evil/code") # value supplied by user
os.execl(user_input11, '/foo/bar', '--do-smth')

# Vulnerable
user_input12 = request.args.get("cat /etc/passwd") # value supplied by user
os.execve("/bin/bash", ["/bin/bash", "-c", user_input12], os.environ)


# Vulnerable
user_input13 = request.args.get("cat /etc/passwd") # value supplied by user
loop = asyncio.new_event_loop()
# This is similar to the standard library subprocess.Popen class called with shell=True
loop.subprocess_shell(asyncio.SubprocessProtocol, user_input13)

# Vulnerable
user_input14 = request.args.get("cat /etc/passwd") # value supplied by user
asyncio.subprocess.create_subprocess_shell(user_input14)