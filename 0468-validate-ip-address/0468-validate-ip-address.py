class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        valid_alphabets = 'abcdef'
        def valid_ipv4(ip_list):
            for ip in ip_list:
                if len(ip) < 1 or len(ip) > 4:
                    return False
                for digit in ip:
                    if not digit.isdigit():
                        return False
                if ip[0] == '0' and len(ip) > 1:
                    return False
                if int(ip) > 255 or int(ip) < 0:
                    return False
            return True
        
        def valid_ipv6(ip_list):
            nonlocal valid_alphabets
            for ip in ip_list:
                if len(ip) > 4 or len(ip) < 1:
                    return False
                for digit in ip:
                    if digit not in valid_alphabets and digit not in valid_alphabets.upper() and not digit.isdigit():
                        return False
            return True
        
        if '.' in queryIP:
            ip_list = list(queryIP.split('.'))
            if len(ip_list) == 4 and valid_ipv4(ip_list):
                return "IPv4"
        if ':' in queryIP:
            ip_list = list(queryIP.split(':'))
            if len(ip_list) == 8 and valid_ipv6(ip_list):
                return "IPv6"
        
        return 'Neither'