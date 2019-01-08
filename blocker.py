# Blocks user indicated websites by modifying the /etc/hosts file

import time
import os

def blocker(website, delay):
    # Copy original hosts file and store it in hosts_old
    hosts = open('/etc/hosts', 'r')
    hosts_text = hosts.read()
    hosts.close()
    hosts_old = open('/Users/connorodell/python/blocker/hosts_old', 'w')
    hosts_old.write(hosts_text)
    hosts_old.close()
    # Create blocker block
    blocker_begin = '\n# Begin Blocker Block\n'
    blocker_block = '''0.0.0.0 {}
0.0.0.0 www.{}\n'''.format(website, website)
    blocker_end = '# End Blocker Block'
    new_hosts_text = hosts_text + blocker_begin + blocker_block + blocker_end
    # Write new hosts file
    hosts = open('/etc/hosts', 'w')
    hosts.write(new_hosts_text)
    hosts.close()
    hosts = open('/etc/hosts', 'r')
    print(hosts.read())
    hosts.close()
    # Undo changes after a delay
    time.sleep(delay)
    old_hosts = open('/Users/connorodell/python/blocker/hosts_old', 'r')
    hosts_text = old_hosts.read()
    old_hosts.close()
    hosts = open('/etc/hosts', 'w')
    hosts.write(hosts_text)
    hosts.close()
    hosts = open('/etc/hosts', 'r')
    print(hosts.read())
    hosts.close()
    # Delete the cache file hosts_old
    os.system('rm ~/python/blocker/hosts_old')

__version__ = '0.1'