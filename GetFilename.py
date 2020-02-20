from github import Github

gitHub = Github("dkc1011", "5cbgsfjy")

repo = gitHub.get_user("jimmyrabbit88").get_repo("bpmnFiles")
pulls = repo.get_pulls(state="closed")
files = pulls[0].get_files()

print(files[0].filename)
