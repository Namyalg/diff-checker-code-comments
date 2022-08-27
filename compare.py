import os 
import difflib

# def compare_files(source_file_1, source_file_2):
#     file1 = open(source_file_1).read()
#     file2 = open(source_file_2).read()

#     comments_removed_file1 =  "\n".join([line.strip('\n').strip("\t").strip() for line in file1.split("\n")])
#     comments_removed_file2 =  "\n".join([line.strip('\n').strip("\t").strip() for line in file2.split("\n")])

#     # print(comments_removed_file1)
#     # print(comments_removed_file2)``

#     if comments_removed_file1 != comments_removed_file2:
#         print("Files are not equal")

# 

def preprocess(source_file, target_file):
    with open(source_file) as source_file_handle:
        text = source_file_handle.readlines()
        with open(target_file, 'w') as target_file_handle:
            for line in text:
                if line != "" or line != "\n":
                    line = line.strip().replace('\n', '').strip("\n")
                    if line == '' or line == '\n' or line.startswith('*') or line.startswith('//') or line.startswith('/*'):
                        continue
                    target_file_handle.write(line.strip("\n").strip("\t").strip("") + '\n')

documented_dir = "/mnt/e/moja.canada/Source/moja.modules.cbm/src/"
source_dir = "/mnt/e/can/moja.canada/Source/moja.modules.cbm/src/"

# path to the executable 
cmd = "./a.out"


for file in os.listdir(documented_dir):
    file_name = file.split(".")[0]
    try:
        commented_file = documented_dir + file 
        original_file = source_dir + file
    
        s_preprocess_1_file = "s_" + file_name + "_preprocess_1.txt"
        s_preprocess_2_file = "s_" + file_name + "_preprocess_2.txt"

        t_preprocess_1_file = "t_" + file + "_preprocess_1.txt"
        t_preprocess_2_file = "t_" + file + "_preprocess_2.txt"

        #  remove single and multi line comments from the source and documented files 

        os.system(cmd + " " + commented_file + " " + s_preprocess_1_file)
        os.system(cmd + " " + original_file + " " + t_preprocess_1_file)

        # remove leading * from the source file
        preprocess(s_preprocess_1_file, s_preprocess_2_file)
        preprocess(t_preprocess_1_file, t_preprocess_2_file)


        # compare between the files here
        file_1_text = open(s_preprocess_2_file).read().replace("\n", "")
        file_2_text = open(t_preprocess_2_file).read().replace("\n", "")

        if file_1_text != file_2_text:
            print("___________________________")
            print("ERROR IN " , file)
        else:
            os.system("rm " + s_preprocess_2_file)
            os.system("rm " + t_preprocess_2_file)
        os.system("rm " + s_preprocess_1_file)
        os.system("rm " + t_preprocess_1_file)

    except Exception as err:
        print("***************************\n")
        print("EXCEPTION IN " , file)
        print(err)
        print("***************************\n")
