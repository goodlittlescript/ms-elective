# Bounds the location if it leaves the specified range.
#
# Note the range is [lower,upper) meaning it includes the
# lower value but only goes "up to" the upper value.
def bound_location(location, lower, upper):
    if location >= upper:
        return upper - 1
    elif location < lower:
        return lower
    else:
        return location


class Raindrop:
    def __init__(self, y_location, x_location):
        self.y_location = y_location
        self.x_location = x_location

    def bound_location(self, max_y, max_x):
        self.y_location = bound_location(self.y_location, 0, max_y)
        self.x_location = bound_location(self.x_location, 0, max_x)


class Cloud:
    def __init__(self, y_location, x_location):
        self.y_location = y_location
        self.x_location = x_location

    def move_left(self):
        self.x_location -= 1

    def move_right(self):
        self.x_location += 1

    def bound_location(self, max_y, max_x):
        self.y_location = bound_location(self.y_location, 0, max_y)
        self.x_location = bound_location(self.x_location, 0, max_x)

    def new_raindrop(self):
        return Raindrop(self.y_location, self.x_location)


class Scene:
    def __init__(self):
        self.now = 0
        self.cloud = Cloud(0, 0)
        self.raindrops = []

    def debug_str(self):
        return f"now: {self.now} ({self.cloud.y_location:.0f}, {self.cloud.x_location:.0f}) raindrops: {len(self.raindrops)}"

    def add_raindrop(self):
        raindrop = self.cloud.new_raindrop()
        self.raindrops.append(raindrop)

    def refresh(self, stdscr):
        max_y, max_x = stdscr.getmaxyx()
        ground = max_y - 1

        self.now += 1
        self.cloud.bound_location(max_y, max_x)

        for raindrop in self.raindrops:
            raindrop.bound_location(max_y, max_x)
            stdscr.addstr(raindrop.y_location, raindrop.x_location, " ")

        new_raindrops = []
        for raindrop in self.raindrops:
            raindrop.y_location += 1
            if raindrop.y_location <= ground:
                new_raindrop = Raindrop(raindrop.y_location, raindrop.x_location)
                new_raindrops.append(new_raindrop)
        self.raindrops = new_raindrops

        for raindrop in self.raindrops:
            stdscr.addstr(raindrop.y_location, raindrop.x_location, ".")

        stdscr.addstr(ground, 0, self.debug_str().ljust(max_x - 1, " "))
        stdscr.move(self.cloud.y_location, self.cloud.x_location)
        stdscr.refresh()
