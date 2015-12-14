import requests

username = "" # fill this
password = "" # fill this

totalCommits = 0
totalAdd = 0
totalRemove = 0
overallAdd = 0
overallRemove = 0
commitCount = 0
commits = []
repositories = 0

baseUrlv2 = "https://bitbucket.org/api/2.0"
baseUrlv1 = "https://bitbucket.org/api/1.0"

print ""
print "Stats for {username}".format(username=username)
print ""

r = requests.get("{base}/user/repositories/".format(base=baseUrlv1), auth=(username, password))

repos = r.json()

for repo in repos:
	if repo['owner'] != username:
		continue
	

	repoSlug = repo['slug']
	r = requests.get("{base}/repositories/{username}/{repo}/commits".format(base=baseUrlv2, username=username, repo=repoSlug), auth=(username, password))

	c = r.json()
	commits.extend(c['values'])

	while 'next' in c:
		r = requests.get("{next}".format(next=c['next']), auth=(username, password))
		c = r.json()
		commits.extend(c['values'])

	for commit in commits:
		commitCount += 1

	print "Total commits in {user}/{repo}: {count}".format(user=username, repo=repoSlug, count=commitCount)
	
	totalCommits += commitCount
	repositories += 1;

	commitCount = 0
	commits = []

print ""
print "Total repositories: {count}".format(count=repositories)
print "Total commits: {count}".format(count=totalCommits)




