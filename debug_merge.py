
import os
import binaryDevider

target = "sample.png"

if os.path.exists(os.getcwd() + "\_devided"):
    binaryDevider.merge_file(target, "D:\_Personal\Project\pj_binaryDivider\_devided")

else:
    print("target file don't exist.")


input()