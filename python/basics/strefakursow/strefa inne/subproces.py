
import subprocess

run_shell = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in run_shell.stdout.readlines():
    print(line)


test = str(run_shell.stdout).split("\n")

for el in test:
    print(f"Plik:{el}")

print("Info: {}".format(run_shell.stderr))
retval = run_shell.wait()
