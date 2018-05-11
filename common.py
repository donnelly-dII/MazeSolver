class dimension:
    def __init__(self, w, h):
        self.MAP_WIDTH = w
        self.MAP_HEIGHT = h


def print_map(map, dim):
	print()
	for y in range(0,dim.MAP_HEIGHT):
		v=""
		for x in range(0,dim.MAP_HEIGHT):
			v+=str(map[y][x]);
		printf(v)

def set_map(map, data, dim):
	for y in range(0,dim.MAP_HEIGHT):
		for x in range(0,dim.MAP_WIDTH):
			map[y][x]=int(data[y*dim.MAP_WIDTH+x])

def init_map(dim):
	return [[0 for x in range(dim.MAP_WIDTH)] for x in range(dim.MAP_HEIGHT)]

