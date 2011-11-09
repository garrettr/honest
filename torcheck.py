# This is pydns and can be downloaded from http://pydns.sourceforge.net/ 
import DNS
DNS.DiscoverNameServers()

def tor_check(clientIp, ELPort):
    # derived from:
    # https://svn.torproject.org/svn/check/trunk/cgi-bin/TorCheck.py
    # exit node IP
    splitIp = clientIp.split('.')
    splitIp.reverse()
    ELExitNode = ".".join(splitIp)

    # ELPort set by caller - try 80 (HTTP) and 443 (HTTPS)
    
    # We'll try to reach this host
    # -- How is this chosen?
    ELTarget = "38.229.70.31"
    # This is the ExitList DNS server we want to query
    ELHost = "ip-port.exitlist.torproject.org"

    # Prepare the question as an A record request
    ELQuestion = ELExitNode + "." + ELPort + "." + ELTarget + "." + ELHost
    request = DNS.DnsRequest(name=ELQuestion, qtype='A')

    # Ask the question, load data into answer
    try:
        answer = request.req()
    except DNS.DNSError:
        return 2

    # Parse the answer, decide if it's allowing exits
    # 127.0.0.2 is an exit and NXDOMAIN is not
    if answer.header['status'] == "NXDOMAIN":
        # We're not exiting from a Tor exit
        return 1
    else:
        if not answer.answers:
            # Unexpected data - fail closed
            return 2
        for a in answer.answers:
            if a['data'] != "127.0.0.2":
                return 2
        # if we're here, that's a positive exit answer
        return 0

def get_client_ip(request):
    ip = request.environ.get('REMOTE_ADDR')
    # print request.environ
    #x_forwarded_for = request.environ.get('X_FORWARDED_FOR')
    #if x_forwarded_for:
    #    ip = x_forwarded_for.split(',')[0]
    #else:
    #    ip = request.environ.get('REMOTE_ADDR')

    print "get_client_ip: ", ip

    return ip

def is_using_tor(request):
    '''
    Check if the given IP address in the request is that of
    a known Tor exit node, indicating this request came through the Tor network
    '''
    ip = get_client_ip(request)
    using_tor = tor_check(ip, '80')
    if using_tor != 0:
        # edge case - only HTTPS (port 443) allowed on exit node
        using_tor = tor_check(ip, '443')

    if using_tor == 0:
        return True
    else:
        return False
