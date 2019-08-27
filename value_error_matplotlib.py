import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import numpy as np

def a_plotting_function(X, Y, dX, dY, print_string):

	plt.plot([X-dX, X], [Y-dY, Y])
	plt.text(X, Y, print_string)

X = 0
Y = 0

dX = 1
dY = 2

frames = 30
frameRate = 24
dpi = 300

print_string = 'poetry'

writer = manimation.FFMpegWriter(fps = frameRate, extra_args=['-pix_fmt', 'yuv420p'])

fig, ax = plt.subplots()

ax.set_xlim((X, X + frames * dX))
ax.set_ylim((Y, Y + frames * dY))

with writer.saving(fig, 'my_beautiful_movie.mp4', dpi):

	for frame in range(frames):
		
		X += dX
		Y += dY

		if X > 0.7 * frames:
			X = np.nan

		a_plotting_function(X, Y, dX, dY, print_string)

		writer.grab_frame()