import subprocess

if __name__ == '__main__':
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    print(out)
    if result.returncode == 0:
        if 'PRETTY_NAME="Ubuntu 22.04.2 LTS"' in out and 'VERSION="22.04.2 LTS (Jammy Jellyfish)"' in out:
            print("SUCCESS")
        else:
            print("FAIL")
    else:
        print("FAIL! CODE !=0")
