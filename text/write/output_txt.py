lst = [
    "amplitude envelope - STFT parameters", "sampling rate: ",
    "segment time: ", "input data length: ", "overlap: ", "spectrum length: "
]
txt_file = open("mytxt.txt", "w")
for element in lst:
    txt_file.writelines(element + "\n")
txt_file.close()