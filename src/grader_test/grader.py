#=============#
#   Imports   #
#-------------#

import traceback
import sys
from difflib import Differ

#====================================================#
#  A simple base test class. It compares the output  #
#  of a program (capturing stdout into a file) with  #
#  a given expected output and produces a diff.      #
#                                                    #
#  If something happens during execution (i.e. a     #
#  runtime error), it should be caught and recorded  #
#  to the output stream (see printException()).      #
#                                                    #
#  Gradescope does not provide a full traceback      #
#  when this happens, so it is necessary to pipe     #
#  the exception information to stdout in order for  #
#  the student to be able to see anything on their   #
#  side.                                             #
#----------------------------------------------------#

class TestModule():

    def setUp(self):
        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.infile = "input.txt"
        self.outfile = "output.txt"
        self.expected = "expected.txt"

    def initStreams(self):
        sys.stdin = self.stdin
        sys.stdout = self.stdout

    def setInputFile(self, string):
        self.infile = string

    def setOutputFile(self, string):
        self.outfile = string

    def setExpectedOutput(self, string):
        self.expected = string

    def printException(self, inst):
        print("\n****\nProgram raised an exception!")
        print("Type: {}".format(type(inst)))
        print("Info: {}".format(inst))
        print("Trace:\n=======================================\n{}\n****".format(traceback.format_exc()))

    #=======================================================#
    #   Produces diff for the produced and expected files   #
    #-------------------------------------------------------#
    
    def runDiff(self):
        diff = Differ()

        ##=[ Open the expected and output files
        
        with open(self.outfile, 'r') as f:
            result = f.readlines()
        with open(self.expected, 'r') as f:
            expected = f.readlines()

        diffResult = list(diff.compare(result, expected))
        diffResult = "".join(diffResult)

        resString = "".join(result)
        expString = "".join(expected)

        print("Expected:\n{}\n\nYour output:\n{}\n\nDiff:\n{}".format(expString, resString, diffResult))

        ##=[ For now, return direct comparison
        return resString == expString

    
