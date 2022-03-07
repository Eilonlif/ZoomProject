# Zoom Project
# by Eilon Lifshitz

# Info:
The project is about learning to use selenium and voice-recognition libraries. Other than the libraries there's a lot of background work that went into researching and setting up the best tools for the voice-recognition part. The things needed to be set up before the project:
 - installing `selenium` and a chrome driver in the correct version
 - setting up a sound channel such that the input stream is the output stream (so that the voice recognition could take the zoom meeting sound as an input)
 - installing the voice recognition library (`snowboy`)

# Steps:
step 1:
 - Opening WhatsApp-web via google-chrome using selenium
 - Scanning specified groups for zoom-meeting links
 - Open the zoom link and start step 2

step 2:
 - Implicitly wait for the teacher to say my name
 - If my name is said, play a recording of myself saying I'm present
 - Quit the program (to not say I'm present twice or more)
