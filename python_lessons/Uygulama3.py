import os  #kütüphane 
os.mkdir("gau_files_modified")
directory = "gau_files" 
filelist = os.listdir(directory)
filelist
outputdir = "gau_files_modified"

for file in filelist:
    if file.endswith(".gau"):
        inputfile=open(directory+"/"+file)
        lines=inputfile.readlines()
        inputfile.close()
        outputfile=open(outputdir+"/"+file,"w")
        for line in lines:
            if line.startswith("%nproc=1"):
                pass
            elif line.startswith("%mem"):
                pass
            else:
                 outputfile.write(line)
        outputfile.close()