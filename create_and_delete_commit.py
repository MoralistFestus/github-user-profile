from github import Github

# your github account credentials
username = "MoralistFestus"
password = "xxxxxx"
# initialize github object
g = Github(username, password)

# searching for my repository
repo = g.search_repositories("text-synthesis")[0]
"""
content = "This the content of the file created"
repo.create_file("test.txt", "commit message", content)"""

"""content = open("content.txt", "r").read()

repo.create_file("test.txt", "commit message", content)"""

# create a file and commit n push
repo.create_file("test.txt", "commit message", "content of the file")
     
# delete that created file
contents = repo.get_contents("test.txt")
repo.delete_file(contents.path, "remove test.txt", contents.sha)