import pafy

# open the txt file that contain the link list we want to download
file = open ('WishList.txt', 'r')

# looping through each link in the txt file
for line in file:
    #assing the link to url var
    url = line
    try:
        # move the link to pafy package
         video = pafy.new(url)

        # converting to the best HQ audio available
         audioHQ = video.getbestaudio()
         print(video.title)

        # Download the audio
         audioHQ.download()

    # if the video remove from youtube or something move to the next link
    except:
        pass

# close the test file
file.close()