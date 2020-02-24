import gitlab

#Create Gitlab
gitLab = gitlab.Gitlab('https://gitlab.com', private_token='mn4DkrPwSDRXBLWvz_BB')

#Define Project (Proj ID = 17049578) from User (evan_barry ID = 5480838)
project = gitLab.projects.get(17049578)

#Define Merge Requests that have been merged
mrs = project.mergerequests.list(state="merged")

#Print the most recent Merge Request's source branch to Standard-output
print(mrs[0].source_branch)