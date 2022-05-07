For the file extensions based templates there is a new modifier ><
Everything between >< replaces the file extension, e.g. >*Tc*.mp2< and searched for the file.

Example template for d2v: Source file is 'E:\Media\Red Planet.d2v'

video=D2VSource(***)
audio=LWLibavAudioSource(> Tc*.mp2<)
audioDub(video, audio)

So it will be found: E:\Media\Red Planet Tc*.mp2
You can also use Tc*, then all files starting with 'E:\Media\Red Planet Tc' will be found.
If more than one is found, the first one is taken in alphabetical order.

A more extreme template example for d2v files:

videoSource = ScriptDir() + [***]
videoSource = Exist(videoSource) ? videoSource : ***
audioSource = ScriptDir() + [> Tc*.mp2<]
audioSource = Exist(audioSource) ? audioSource : > Tc*.mp2<
video=D2VSource(videoSource)
audio=LWLibavAudioSource(audioSource)
audioDub(video, audio)

