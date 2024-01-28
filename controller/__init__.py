#__all__=["user_controller","product_controller"]
import os
import glob
#init so that python treat it as a package
__all__=[os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")] #to import all the files in the folder