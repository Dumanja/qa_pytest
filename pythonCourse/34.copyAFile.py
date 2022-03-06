# copyfile() =      copies contents of a file
# copy() =          copyfile() + permission mode + destination can be a diretory
# copy2() =         copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copy2('C:\\Users\\Topalovic\\Desktop\\text.txt', 'C:\\Users\\Topalovic\\Desktop\\copy.txt') #src.dst
