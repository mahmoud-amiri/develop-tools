import shutil
import subprocess

def copy_and_run_questa_sim_bat():
    src = f"./script/questa_sim.bat"
    with open(src, 'r') as f:
        first_line = f.readline().strip()
        if first_line.startswith('::'):
            design_name = first_line[3:].strip()
        else:
            design_name = None

    dst = f"./tb/uvmf/project_benches/{design_name}/sim/invoke_questa.bat"
    # Copy the file to the destination
    shutil.copy(src, dst)
    
    # Run the copied file
    subprocess.run(dst, shell=True)

