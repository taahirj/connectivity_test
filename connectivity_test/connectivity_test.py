'''
Created on 26 November 2021

Test connectivity to a given host and port within a given timeout period.

Functions:
    - connectivity_test(host, port, timeout)
      Keyword arguments:
          host (str) -- Hotname or IP Address (*Required)
          port (int) -- Port number (*Required)
          timeout (int) -- Timeout in seconds (*Required)
          ** Note: Defaults applies when run as main. See --help for details.
      Returns:
          str -- True if connection is successful else False if not successful
              -- String of error is returned if the function is called incorrectly
          ** Note: Prints to terminal when running as main

Usage: Can be run as a standalone script, called directly or imported in other programs.

@author: Taahirj
'''

import socket
   
def connectivity_test(host: str, port: int, timeout: int) -> str:
    """Test connectivity to a given host and port within a given timeout period.

    Keyword arguments:
        host (str) -- Hotname or IP Address (*Required)
        port (int) -- Port number (*Required)
        timeout (int) -- Timeout in seconds (*Required)
    Returns:
          str -- True if connection is successful else False if not successful
              -- String of error is returned if the function is called incorrectly
    """

    styles = {
                 "PURPLE":"\033[1;35;48m",
                 "CYAN": "\033[1;36;48m",
                 "BOLD": "\033[1;37;48m",
                 "BLUE": "\033[1;34;48m",
                 "GREEN": "\033[1;32;48m",
                 "YELLOW": "\033[1;33;48m",
                 "RED": "\033[1;31;48m",
                 "BLACK": "\033[1;30;48m",
                 "UNDERLINE": "\033[4;37;48m",
                 "END": "\033[1;37;0m"
             }
    
    # Check that host is not empty then check that port and timeout are positive integers before testing connectivity
    if bool(host.strip()) is not True:
        if __name__ == "__main__":
            print("Hostname is empty. Exiting...")
            quit()
        return "ERROR: Hostname is empty."
    if str(port).isdigit() is not True:
        if __name__ == "__main__":
            print("Port is not a positive integer. Exiting...")
            quit()
        return "ERROR: Port is not a positive integer."
    elif str(timeout).isdigit() is not True:
        if __name__ == "__main__":
            print("Timeout is not a positive integer. Exiting...")
            quit()
        return "ERROR: Timeout is not a positive integer."
    else:
        host = str(host)
        port = int(port)
        timeout = int(timeout)


    try:
        if __name__ == "__main__":
            print("---Connectivity Test------------")
            print("To: " + styles["CYAN"] + str(host) + ":" + str(port) + styles["END"])
            print("Timeout: " + styles["CYAN"] + str(timeout)  + " seconds" + styles["END"])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(int(timeout))
        result = sock.connect_ex((str(host),int(port)))
        if result == 0:
            if __name__ == "__main__":
                print(styles["GREEN"] + "REACHABLE" + styles["END"] +": Host/IP " + str(host) + " is REACHABLE on Port " + str(port))
            return "True"
        else:
            if __name__ == "__main__":
                print(styles["RED"] + "UNREACHABLE" + styles["END"] + ": Host/IP " + str(host) + " is UNREACHABLE on Port " + str(port))
            return "False"
    
    except KeyboardInterrupt:
        if __name__ == "__main__":
            print(styles["RED"] + "ERROR" + styles["END"] + ": Keyboard interrupt detected, you pressed Ctrl+C. Exiting...")
            sock.close()
            quit()
        return "ERROR: Keyboard interrupt detected."
    
    except socket.gaierror:
        if __name__ == "__main__":
            print(styles["RED"] + "ERROR" + styles["END"] + ": Invalid hostname or IP Address, could not be resolved. Exiting...")
            quit()
        return "ERROR: Invalid hostname or IP Address, could not be resolved."
    
    except socket.error:
        if __name__ == "__main__":
            print(styles["RED"] + "ERROR" + styles["END"] + ": Socket error, could not connect to server")
            quit()
        return "ERROR: Socket error, Could not connect to server"
    
    sock.close()
    if __name__ == "__main__":
        print("---Connectivity Test Complete---")

if __name__ == "__main__":

    from optparse import OptionParser

    # Set up possible command line options
    usage = "Usage: python3 %prog [option1] arg1 [option2] arg2 ..."
    parser = OptionParser(usage=usage, version="%prog 1.0", description="Tests connectivity to a given host/ip and port based on options specified. If no options are specified then options marked with (default) will be used.", epilog="Created by Taahirj to hopefully make things easier when testing connectivity where tools like telnet are not available.")
    parser.add_option("-i", "--host", action="store", type="string", dest="host", help="Hostname or ip address: www.google.com (default)", default="www.google.com")
    parser.add_option("-p", "--port", action="store", type="string", dest="port", help="Port number: 443 (default)", default="443")
    parser.add_option("-t", "--timeout", action="store", type="string", dest="timeout", help="Timeout in seconds: 5 (default)", default="5")

    (options, args) = parser.parse_args()

    host = options.host
    port = options.port
    timeout = options.timeout

    connectivity_test(host, port, timeout)


