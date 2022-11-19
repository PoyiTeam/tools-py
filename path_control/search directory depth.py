import glob,os.path
filesDepth3 = glob.glob('*/*/*')
dirsDepth3 = filter(lambda f: os.path.isdir(f), filesDepth3)