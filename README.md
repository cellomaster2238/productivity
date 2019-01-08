# productivity
For Mac OS X. Block certain websites to avoid time sinks

v0.1
    blocker prevents access to a webpage by zeroing out the ip address of a website
    in the /etc/hosts file on OS X. Administrator privileges are required.
    
    Ex: blocker(website, time)
        webside should be a string of the form 'name.com'
        time is a duration in seconds

v0.2 - proposed
    blocker can read in a list of websites to block from a text file
    
    smarter handling of /etc/hosts file to prevent errors that could occur if another
    program makes changes to the file while blocker is running
