import glob

path =  input("Enter folder where video and subtitle file present : ")
videoFormat =  input("Enter the video format Eg) mkv, mp4 ; ")
subtitleFormat =  input("Enter the video format Eg) srt : ")
videoFiles = glob.glob(path+"/*.mkv")
subtitleFiles = glob.glob(path+"/*.srt")
if(len(videoFiles) == len(subtitleFiles)):
    for i in range(0,len(videoFiles)):
        print(videoFiles[i],subtitleFiles[i])
        os.rename(subtitleFiles[i],videoFiles[i][:-3]+"srt")
else:
    print("No fo subtitile and video files are not same")
