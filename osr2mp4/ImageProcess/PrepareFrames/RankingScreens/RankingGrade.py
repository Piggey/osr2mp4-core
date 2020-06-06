from ...PrepareFrames.YImage import YImage

ranking = "ranking-"


def prepare_rankinggrade(scale, settings):
	frames = []

	grades = ["X", "S", "A", "B", "C", "D"]
	for grade in grades:
		frames.append(YImage(ranking + grade, settings, scale).img)

	return frames
