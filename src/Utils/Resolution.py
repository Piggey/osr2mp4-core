def get_screensize(width, height):
	playfield_width, playfield_height = width * 0.8 * 3 / 4, height * 0.8  # actual playfield is smaller than screen res
	playfield_scale = playfield_width / 512
	scale = height / 768
	move_right = round(width * 0.2)  # center the playfield
	move_down = round(height * 0.1)
	return playfield_scale, playfield_width, playfield_height, scale, move_right, move_down

