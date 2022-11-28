
import subprocess

run_shell = subprocess.run(['ls', './echo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

test = str(run_shell.stdout.decode()).split('\n')

for el in test:
    if not el:
        continue
    print(f"Plik: {el}")
print("Info: {}".format(run_shell.stderr.decode()))
