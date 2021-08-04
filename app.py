import http.server
import socketserver
import wget
def share():
    #line
    PORT = 2038
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Server started at localhost:" + str(PORT))
        httpd.serve_forever()
def accept():
    ip=input("[+] Enter Ip address of senter:")
    file=input("[+] Enter File name to get:")
    url="http://"+str(ip)+":2038/"+str(file)
    wget.download(url)
def main():
    print("-FIL3-")
    option=input("[1] Sent\n[2] Recive\n[+] Select Option:")
    if(int(option) == 1):
        print("[+] Share Option Started\n")
        print("[+] Please Connect You and Reciver on same WIFI\n")
        print("[+] Please Share your local IP with Reciver\n")
        share()
    if(int(option) == 2):
        print("[+] Recive Mode Started\n")
        accept()
main()
