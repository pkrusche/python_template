#!/usr/bin/env python

import module


def main():
    t = module.TestClass()
    print "Our version is: %s" % module.__version__
    print t.answer_me("What is the answer to the ultimate question?")

if __name__ == "__main__":
    main()