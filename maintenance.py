import platform
import subprocess
from time import sleep

def announce_script():
    print("┌──────────────────────────────────────────────────┐")
    print("│┼────────────────────────────────────────────────┼│")
    print("││                   Maintenance                  ││")
    print("││                                                ││")
    print("││ver. 230406A                                 -JT││")
    print("│┼────────────────────────────────────────────────┼│")
    print("└──────────────────────────────────────────────────┘")

def run_command(command, description):
    print(f"┌──────────────────────────────────────────────────┼")
    print(f"| {description}")
    print(f"|                                                  ┼")
    try:
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=600, shell=True, check=True)
        print(f"| {completed_process.stdout.strip()}{' '*(50-len(description)-len(completed_process.stdout.strip()))}(DONE) |")
        print("└──────────────────────────────────────────────────┘")
    except subprocess.CalledProcessError as e:
        print(f"| {e.stderr.strip()}{' '*(50-len(description)-len(e.stderr.strip()))}(ERROR) |")
        print("└──────────────────────────────────────────────────┘")

def main():
    print("Script started.")
    announce_script()

    os_version = platform.system()
    if os_version == "Windows":
        release_version = platform.release()
        if release_version.startswith("10"):
            run_command("dism /Online /Cleanup-image /Restorehealth", "Running: Deployment Image Servicing and Management")
            run_command("sfc /scannow", "Running: System File Checker")
            run_command("net stop wuauserv", "Stopping: Windows Update Service")
            run_command('del /s /q "C:/Windows/Temp"', "Deleting: C:\Windows\Temp")
            run_command('del /s /q "C:/Windows/SoftwareDistribution"', "Deleting: C:\Windows\SoftwareDistribution")
            run_command("sc config wuauserv start=auto", "Configuring: Windows Update Service")
            run_command("net start wuauserv", "Starting: Windows Update Service")
            run_command("USOCLIENT.EXE RefreshSettings StartScan StartDownload ScanInstallWait StartInstall", "Installing: Updates")
        else:
            print("┌──────────────────────────────────────────────────┐")
            print("│Unsupported Windows version               (ERROR) │")
            print("└──────────────────────────────────────────────────┘")
    else:
        print("┌──────────────────────────────────────────────────┐")
        print("│Unsupported Operating System              (ERROR) │")
        print("└──────────────────────────────────────────────────┘")

    print("┌──────────────────────────────────────────────────┐")
    print("│                    Complete                      │")
    print("└──────────────────────────────────────────────────┘")
    print("Script finished.")
    sleep(120)

if __name__ == '__main__':
    main()
