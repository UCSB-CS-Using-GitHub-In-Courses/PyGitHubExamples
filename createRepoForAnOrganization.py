#!/usr/bin/python                                                                    

import sys
sys.path.append("./PyGithub");
from github import Github

import getpass
import argparse


from github import Github
from github import GithubException

parser = argparse.ArgumentParser(description='List all repos for an org')
parser.add_argument('orgName',help='github Organization name')

args = parser.parse_args()

username = raw_input("Github Username:")
pw = getpass.getpass()
g = Github(username, pw)
orgName = args.orgName

try:
    org = g.get_organization(orgName)
except GithubException as ghe:
    print(ghe)

try:
    org.create_repo(
        "myNewRepo", # name -- string
        "My new repo, created using PyGithub", # description -- string
        "http://www.example.org", # homepage -- string
        True, # private -- bool
        True, # has_issues -- bool
        True, # has_wiki -- bool
        True, # has_downloads -- bool
        auto_init=True,
        gitignore_template="Python")

    # You could also set team_id= to something of type github.Team.Team

except GithubException as ghe:
    print(ghe)




