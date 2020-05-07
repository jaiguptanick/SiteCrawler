from mkdir import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

root_dir = "Target URL Results"
create_dir(root_dir)

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F ', ip_address)
    whois = get_whois(domain_name)
    robots_txt = get_robots_txt(url)
    create_report(name, url, domain_name, nmap, robots_txt, whois)
    
def create_report(name, fullurl, domain_name, nmap, robots_txt, whois):
    project_dir = root_dir + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/fullurl.txt', fullurl)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/whois.txt', whois)
    write_file(project_dir + '/robots_txt.txt', robots_txt)
    print("done:)\n" + "results are located in Target URL Results/" + name + "/")

gather_info('HOSTNAME', 'HOSTURL')

