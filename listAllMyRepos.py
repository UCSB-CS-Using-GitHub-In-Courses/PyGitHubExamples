    #!/usr/bin/python
    
    import getpass
    import sys
    
    # In the main directory of the repo where you are developing with PyGithub,
    # type:
    #    git submodule add git://github.com/jacquev6/PyGithub.git PyGithub
    #    git submodule init
    #    git submodule update
    #
    # That will populate a PyGithub subdirectory with a clone of PyGithub
    # Then, to add it to your Python path, you can do:
    
    sys.path.append("./PyGithub");
    
    from github import Github
    from github import GithubException
    
    username = raw_input("Github Username:")
    pw = getpass.getpass()
    g = Github(username, pw)
    
    for repo in g.get_user().get_repos():
        print (repo.name)

