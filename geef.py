import glitch
import subprocess

def make_gif(filename, paths, duration=10):
	subprocess.call(['convert', '-delay', '20', '-loop', '0'] + paths + [filename])

glitcher = glitch.Glitch()


frames = []
glitched_image = 'gif/ken/ken-283-glitched.jpg'
total_mentions = 20

for i in range(0, total_mentions):
	glitched_image = glitcher.trigger(glitched_image, "random")
	print glitched_image
	frames.append(glitched_image)

make_gif("mygif.gif", frames)

# make_gif("mygif.gif", ["ken/ken-109-glitched.jpg", "ken/ken-118-glitched.jpg", "ken/ken-121-glitched.jpg"])
