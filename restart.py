import psutil, subprocess, os, signal

script_name="xl8.py"
# PROCNAME = "python.exe"

# for proc in psutil.process_iter():
#     print(proc)
#     #print(dir(proc))
#     # check whether the process name matches
#     if proc.name() == PROCNAME:
#         proc.kill()


#out=os.popen("ps ax | grep " + name + " | grep -v grep")
#out=os.popen("ps wx | grep " + name + " | grep -v grep")
out=os.popen("ps wx")
for line0 in out:
    fields = line0.split()
    pid = fields[0]
    if script_name in line0:
        os.kill(int(pid), signal.SIGKILL)    
        print(f"killed process:", fields)
    #print([ot])
#print(out)

out2=os.popen("nohup python %s &"%script_name)
#for line0 in out2: print(line0)