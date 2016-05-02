"""
Generate the new python project.
Follow instructions carefully.

Author: Ronen Ness
Since: 2016
"""
import colorama
import shutil
import re

colorama.init()

def print_err(msg):
    print "> " + colorama.Fore.RED + msg.capitalize() + colorama.Style.RESET_ALL

def validate_input(name, forwhat, allow_spaces=False, english_only=True, min_len=1, allow_special_chars=""):
    """
    make sure an input is valid
    """
    # strip whitespaces
    name = name.strip()

    # validate english and dashes / underscores only
    if english_only:
        to_check = name
        for sc in allow_special_chars:
            to_check = to_check.replace(sc, "")
        if not re.match("^[\w\d_-]*$", to_check):
            print_err ("> Invalid characters in %s!" % forwhat)
            return False

    # make sure length is valid
    if len(name) < min_len:
        print_err ("%s is too short!" % forwhat)
        return False

    # no spaces
    if not allow_spaces and " " in name:
        print_err ("%s cannot contain spaces!" % forwhat)
        return False

    # make sure actually got characters
    if min_len > 0 and len(name.replace("_", "").replace("-", "")) == 0:
        print_err ("Invalid %s!" % forwhat)
        return False
    
    # return name
    return name

def get_input(msg, forwhat, allow_spaces=False, english_only=True, min_len=1, allow_special_chars=""):
    """
    get input, validate it, and repeat until getting valid values
    """
    inpt = False
    while inpt is False:
        inpt = raw_input(msg + " ")
        inpt = validate_input(inpt, forwhat, allow_spaces, english_only, min_len, allow_special_chars)
    return inpt


print ""
print colorama.Style.BRIGHT + "This script will generate a PyPi package structure for your project! Please fill in the some details to begin.." + colorama.Style.RESET_ALL
print ""

# get author name
author_name = get_input("Author name (eg 'John Doe'):", "author name", True, False, allow_special_chars=" ")

# get project name
project_name = get_input("Project name (use CamelCase, eg 'MyCoolProject'):", "project name", False, True)
project_name_lower = project_name.lower().replace('-', '_')

# get package name
package_name = get_input("Package name (leave blank for '%s'):" % project_name_lower, "package name", False, True, 0).replace('-', '_')
if len(package_name) == 0:
    package_name = project_name_lower

# get author email
default_email = author_name.replace(' ', '.').lower() + "@gmail.com"
author_email = get_input("Author email (leave blank for '%s'):" % default_email, "author email", True, True, 0, allow_special_chars=".@")
if len(author_email) == 0:
    author_email = default_email

# get git url
default_git = "https://github.com/%s/%s" % (author_name.replace(" ", ""), project_name)
git_url = get_input("Project git url (leave blank for '%s'):" % default_git, "git url", True, False, 0)
if len(git_url) == 0:
    git_url = default_git

# get description and tags
desc = get_input("Project short description (eg 'Lib to do X for Y.'):", "project description", True, False, 0)
tags = get_input("Project Tags, separate with comma (eg 'search,find,db'):", "project tags", True, True, 0, allow_special_chars=" ,")

# break tags into a list and strip all tags against whitespace etc.
tags = tags.split(",")
tags = [tag.strip() for tag in tags]

# make sure its all correct
print ""
print colorama.Style.BRIGHT + "Done! please confirm final details.." + colorama.Style.RESET_ALL
print "Project name: " + colorama.Fore.GREEN + project_name + colorama.Style.RESET_ALL
print "Package name: " + colorama.Fore.GREEN + package_name + colorama.Style.RESET_ALL
print "Author name: " + colorama.Fore.GREEN + author_name + colorama.Style.RESET_ALL
print "Author email: " + colorama.Fore.GREEN + author_email + colorama.Style.RESET_ALL
print "Git: " + colorama.Fore.GREEN + git_url + colorama.Style.RESET_ALL
print "Description: " + colorama.Fore.GREEN + desc + colorama.Style.RESET_ALL
print "Tags: " + colorama.Fore.GREEN + unicode(tags) + colorama.Style.RESET_ALL
raw_input("Hit enter to proceed, ctrl+c to abort.")

# create the project dir
shutil.copytree("Template", project_name)

# replace all tags
import os
import fileter

class ReplaceWords(fileter.FilesIterator):
    """
    Iterate over files and replace project settings
    """
    def process_file(self, path, dryrun):

        if dryrun:
            return path

        with open(path, "r") as infile:
            content = infile.read()

        content = content.replace("<PACKAGE_NAME>", project_name)
        content = content.replace("<PACKAGE_NAME_LOWER>", package_name)
        content = content.replace("<AUTHOR_NAME>", author_name)
        content = content.replace("<AUTHOR_EMAIL>", author_email)
        content = content.replace("<GIT_REPO>", git_url)
        content = content.replace("<PACKAGE_ONELINER>", desc)
        content = content.replace("<KEYWORDS>", unicode(tags))

        with open(path, "w") as outfile:
            outfile.write(content)

it = ReplaceWords()
it.add_folder(project_name)
it.process_all()

# rename source dir
src_dir = os.path.join(project_name, package_name)
os.rename(os.path.join(project_name, "src"), src_dir)

print ""
print colorama.Style.BRIGHT + ("All Done! Your package is at '%s'." % project_name) + colorama.Style.RESET_ALL
print "What's left to do:"
print "1. Write the actual code in %s." % src_dir
print "2. Fill in the readme file %s." % os.path.join(project_name, "README.md")
print "3. Write tests in %s." % os.path.join(project_name, "tests")
print "4. Validate setup.py content and upload your package!"
raw_input("")
