#================================================#
#   A suite for tests the autograders may use.   #
#------------------------------------------------#

from difflib import Differ

#=======================================================#
#   Produces diff for the produced and expected files   #
#-------------------------------------------------------#
    
def runDiff(file1, file2):
    diff = Differ()

    ##=[ Open the expected and output files
    
    with open(file1, 'r') as f:
        result = f.readlines()
    with open(file2, 'r') as f:
        expected = f.readlines()

    diffResult = list(diff.compare(result, expected))
    diffResult = "".join(diffResult)

    resString = "".join(result)
    expString = "".join(expected)

    print("Expected:\n{}\n\nYour output:\n{}\n\nDiff:\n{}".format(expString, resString, diffResult))

    ##=[ For now, return direct comparison
    return resString == expString