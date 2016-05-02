from distutils.core import setup
import os

# get curr dir
curr_dir = os.path.abspath(os.path.dirname(__file__))

# get readme
with open(os.path.join(curr_dir, 'README.md')) as readme_file:
    long_desc = readme_file.read()

# setup
setup(
  name = '<PACKAGE_NAME_LOWER>',
  packages = ['<PACKAGE_NAME_LOWER>'],
  package_data = {'<PACKAGE_NAME_LOWER>' : ["*.py", "README.md"], },
  version = '1.0.0',
  description = '<PACKAGE_ONELINER>',
  author = '<AUTHOR_NAME>',
  author_email = '<AUTHOR_EMAIL>',
  url = '<GIT_REPO>',
  download_url = '<GIT_REPO>/tarball/1.0.0',
  long_description = long_desc,
  keywords = <KEYWORDS>,
  classifiers = [],
)
