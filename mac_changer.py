import subprocess

NEW_MAC = input("NEW MAC > ")
interface = input("interface > ")

print("[+] Changing Mac Address to " + NEW_MAC )

subprocess.call("ifconfig " +interface + " down", shell=True)
subprocess.call("ifconfig " +interface + " hw ether " + NEW_MAC , shell=True)
subprocess.call("ifconfig " +interface + " up", shell=True)

print("[+] Mac Address Changed Successfully")

print("[+] Thanks for downloading on my Github page")

print("[+] To check if MAC Address changed type 'ifconfig' in terminal")

print("[+] Thanks for your kind understanding")