from subprocess import (PIPE,run)

DATA_DIR = './data/'

if __name__ == "__main__":
    filename = input("Enter filename: ")
    try :
        input_filedir = DATA_DIR + filename
        with open(input_filedir, "r") as fi :

            if fi is None:
                raise FileNotFoundError("File not found")


            output_filedir = DATA_DIR + "detailed-" + filename + ".md"
            fo = open(output_filedir, "w")
            for line in fi:
                line =  line.strip()
                if len(line) == 0:
                    break
                if line[0] == '#' :
                    continue

                fo.writelines("## " + line + "\n")
                fo.writelines("### meaning " + "\n")
                result = run(["wd", line],stdout=PIPE, stderr=PIPE, universal_newlines=True)
                meaning = result.stdout.replace("", " ")
                meaning = meaning.replace("[31m", "")
                meaning = meaning.replace("[32m", "")
                meaning = meaning.replace("[36m", "")
                meaning = meaning.replace("[33m", "")
                meaning = meaning.replace("[34m", "")
                meaning = meaning.replace("[35m", "")
                meaning = meaning.replace("[0m", "")
                fo.writelines(meaning)
                fo.writelines("\n")
                fo.flush()

        fo.flush()
        fo.close()
    except Exception as e:
        print(e)


