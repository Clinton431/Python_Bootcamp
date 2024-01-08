#copyfile() = copies content of a file
# copy () = copyfile() + permission mode + destination can be a directory
# copy() = copy() + copies metadata (files's creation and modification times)
import shutil

shutil.copyfile('test.txt','copy-file.txt') #src, dest