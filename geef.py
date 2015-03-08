import glitch
import subprocess
import tumblr

def make_gif(filename, paths, duration=10):
	subprocess.call(['convert', '-delay', '20', '-loop', '0'] + paths + [filename])

glitcher = glitch.Glitch()

def get_caption(titles):
	caption = ""
	for title in titles:
		caption += title + '\n'
	return caption

tumblr.search_party()

frames = []
glitched_image = tumblr.searchTerm + '.jpg'
total_mentions = 20

for i in range(0, total_mentions):
	glitched_image = glitcher.trigger(glitched_image)
	print glitched_image
	frames.append(glitched_image)

make_gif("mygif.gif", frames)

# make_gif("mygif.gif", ["ken/ken-109-glitched.jpg", "ken/ken-118-glitched.jpg", "ken/ken-121-glitched.jpg"])

ouath_data = open("oauth.txt")

# get all keys
keys = ouath_data.read()
keys_decoded = keys.decode("utf-8-sig")
keys = keys_decoded.encode("utf-8")
keys = keys.rstrip().split('\n')


client = pytumblr.TumblrRestClient(
  keys[0],
  keys[1],
  keys[2],
  keys[3]
)

# post photo to tumblr
client.create_photo("anarchyarchive", caption=get_caption(tumblr.new_titles), state="published", data = "mygif.gif" )