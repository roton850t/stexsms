import platform
import sys
import proxy_XD

def main():
    if platform.architecture()[0] == "64bit":
        proxy_XD.main()
    else:
        print("32bit Not Supported! Sorry")
        sys.exit(1)

if __name__ == "__main__":
    main()
