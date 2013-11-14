#!/usr/bin/env python

import pkg_resources

# replace with your package name from setup.py
__version__ = pkg_resources.require("template_project")[0].version


class TestClass:
    """ A test class to demonstrate our template python module
    """

    def __init__(self):
        pass

    #noinspection PyMethodMayBeStatic
    def answer_me(self, question):
        """ Returns an answer

        :param question: the question
        :return: the answer
        """
        return "The answer to '%s' is: 42" % question, 42
