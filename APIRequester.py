import gitlab

#Create Gitlab
gitLab = gitlab.Gitlab('https://gitlab.com', private_token='mn4DkrPwSDRXBLWvz_BB')

#Define Project (Proj ID = 17049578) from User (evan_barry ID = 5480838)
project = gitLab.projects.get(17049578)

def getMergingCommitId(sourceBranch):
    commits = project.commits.list()
    for com in commits:
        if (com.title == "Merge branch '" + sourceBranch + "' into 'master'"):
            return com.short_id

    return 'No ID found'

#Define Merge Requests that have been merged
mrs = project.mergerequests.list(state="merged")
sourceBranch = mrs[0].source_branch

commitId = getMergingCommitId(sourceBranch)

if(commitId != 'No ID found'):
    commit = project.commits.get(commitId)
    #first - 4ab347b4
    #second - 7d6d3893

    masterChanges = commit.diff()

    filename = masterChanges[0]['new_path']

    filenameClipped = filename[:-5]

    print(filenameClipped)
else:
    print('')





