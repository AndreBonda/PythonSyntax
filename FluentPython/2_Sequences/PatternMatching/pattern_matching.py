class Robot:

    def handle_command(self, message):
        match message:
            case ['BEEPER', frequency, times]:
                self.beep(times, frequency)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case _:
                raise ValueError("Invalid command")
    
    def beep(self, frequency, times):
        print(f"Beep: {frequency}, {times}")

    def rotate_neck(self, angle):
        print(f"Rotate neck: {angle}")

    def beep(self, ident, intensity):
        print(f"Led: {ident}, {intensity}")
            
robot = Robot()
robot.handle_command(['BEEPER', 1, 10])
robot.handle_command(('Neck', 90))
# robot.handle_command(['Invalid']) # raise an exception

# pattern matching with nested tuples

def areas_matching(areas):
    for a in areas:
        match a:
            case [name, _, (lat,lon)] if lon > 0:
                print(a)

areas_matching(
    [
        ('Tokyo', 'JP', (35.43343, 139.2433253)),
        ('Rome', 'IT', (12.43343, 23.2433253)),
        ('Mexico City', 'MX', (7.65464, -67.45454)),
        ('New York', 'US', (12.43343, -1.2433253)),
    ]
)