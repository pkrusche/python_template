#!/usr/bin/env python

""" Git Versioning Script

Will transform stdin to expand some keywords with git version/author/date information.

Specify --clean to remove this information before commit.

Setup:

1. Copy version.py into your git repository

2. Run:

   git add version.py
   python version.py

   Use a different version of python if necessary.

3. The version will be usable in a module like this:

    # replace with your package name from setup.py
    __version__ = ""

"""

__version__ = ""
__author__ = ""
__email__ = ""
__date__ = ""


import sys
import subprocess
import re
import os
import argparse


def main():
    parser = argparse.ArgumentParser("Python versioning script")

    python_executable = os.path.normpath(sys.executable).replace("\\", "/")

    parser.add_argument("--smudge", "-s", dest="smudge", action="store_true")
    parser.add_argument("--clean", "-c", dest="clean", action="store_true")
    parser.add_argument("--install", "-i", dest="install", action="store_true")
    parser.add_argument("--force", "-f", dest="force", action="store_true")

    args = parser.parse_args()

    smudge = args.smudge
    clean = args.clean
    install = args.install
    force = args.force

    if install:
        subprocess.check_call(["git", "config", "filter.versioning.smudge",
                               "%s version.py --smudge" % python_executable])
        subprocess.check_call(["git", "config", "filter.versioning.clean",
                               "%s version.py --clean" % python_executable])
        try:
            subprocess.check_call(["grep",  "^version.py filter=versioning",
                                   ".gitattributes"])
        except subprocess.CalledProcessError:
            os.system("echo version.py filter=versioning >> .gitattributes")

        updates = """
#!/bin/sh

PYTHON="%s"

cat version.py | $PYTHON version.py --clean --smudge > __version_tmp.py
mv __version_tmp.py version.py

""" % python_executable
        pcohook = os.path.join(".git", "hooks", "post-commit")
        pcmhook = os.path.join(".git", "hooks", "post-checkout")
        if (os.path.exists(pcohook) or os.path.exists(pcmhook)) and\
           not force:
            print """
Failed:

.git/hooks/post-commit and post-checkout appear to exist already, and --force was
not specified. If you have custom hooks, please include this line to automatically
update software versions:

%s
""" % updates
            exit(1)

        with open(pcohook, "w") as f:
            f.write(updates)
        with open(pcmhook, "w") as f:
            f.write(updates)
    else:
        # initialise empty here. Otherwise: forkbomb through the git calls.
        if smudge:
            subst_list = {
                # '--dirty' could be added to the following, too, but is not supported everywhere
                "version": subprocess.check_output(['git', 'describe', '--always']),
                "date": subprocess.check_output(['git', 'log', '--pretty=format:"%ad"', '-1']),
                "author": subprocess.check_output(['git', 'log', '--pretty=format:"%an"', '-1']),
                "email": subprocess.check_output(['git', 'log', '--pretty=format:"%ae"', '-1'])
            }
        else:
            subst_list = {
                "version": "",
                "date": "",
                "author": "",
                "email": ""
            }

        for line in sys.stdin:
            if clean:
                for k in subst_list:
                    rexp = "__%s__\s*=.*" % k
                    line = re.sub(rexp, "__%s__ = \"\"" % k, line)

            if smudge:
                for k, v in subst_list.iteritems():
                    v = re.sub(r'[\n\r\t"\']', "", v)
                    rexp = "__%s__\s*=[\s'\"]+" % k
                    line = re.sub(rexp, "__%s__ = \"%s\"\n" % (k, v), line)
            sys.stdout.write(line)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print str(e)
        exit(1)
