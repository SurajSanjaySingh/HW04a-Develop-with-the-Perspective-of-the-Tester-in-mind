"""
Created on Fri Feb 22 18:44:01 2023

@author: Suraj

Homework: 04a - Develop with the Perspective of the Tester in mind
"""
def my_brand(assignment):
  import datetime
  current_time = datetime.datetime.now()
  print("\n=*=*=*= Suraj Sanjay Singh =*=*=*=")
  print("=*=*=*= Course 2023S-SSW567-A =*=*=*=")
  print("=*=*=*= " + assignment + " =*=*=*=")
  print("=*=*=*= " + current_time.strftime("%m/%d/%Y, %H:%M:%S") + " =*=*=*=\n")
    
    
import requests

def getCommit(user,name):
    getCommit_url ="https://api.github.com/repos/"+f'{user}' +"/" + name + "/commits"
    commitResp = requests.get(getCommit_url)
    commitResp_json = commitResp.json()
    value1=len(commitResp_json)
    return value1   


def getRepo(user):
    getRepo_url = "https://api.github.com/" + "users" + "/" + f'{user}' + "/repos"
    response = requests.get(getRepo_url)
    repo_json = response.json()
    if len(repo_json) != '':
        for i in repo_json:
            num = getCommit(f'{user}',f'{i["name"]}')
            print(f'Repository name: {i["name"]} and Number of commits: {num}')
        return 'Success'    
    else:
        return 'Wrong Attempt'

 
def main():
    user = input("Please Enter the GitHub User Id: ")
    getRepo(user)
   

if __name__ == "__main__":
    main()    
