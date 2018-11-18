import subprocess
import io

args = 'ls -l'
#args = ['ls','-l']

proc = subprocess.Popen( args, shell=True, stdout=subprocess.PIPE)
for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
  print(line)
