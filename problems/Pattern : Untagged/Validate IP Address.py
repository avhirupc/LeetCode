def validIPv4(IP):
    IPs=IP.split(".")
    if len(IPs)!=4:
        return False
    mem=set([str(d) for d in range(10)])
    for sn in IPs:
        try:
            if len(set(sn)-mem)>0:
                return False
            if (sn[0]=="0" and int(sn)!=0) or (sn[0]=="0" and int(sn)==0 and len(sn)>1):
                return False
            if not (0<=int(sn)<=255):
                return False
        except:
            return False
    return True

def validIPv6(IP):
    IPs=IP.split(":")
    valid_c=set([str(d) for d in range(10)]+["a","b","c","d","e","f"])
    if len(IPs)!=8:
        return False
    for sn in IPs:
        if len(sn)>4 or len(sn)==0:
            return False
        sn=sn.lower()
        if len(set(sn)-valid_c)>0:
            print(set(sn)-valid_c,sn)
            return False
    return True
        
    
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if "." in IP and validIPv4(IP):
            return "IPv4"
        elif ":" in IP and validIPv6(IP):
            return "IPv6"
        else:
            return "Neither"
        