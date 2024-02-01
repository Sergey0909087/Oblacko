import arcade

def create_cloud(x,y):
    arcade.draw_circle_filled(
        center_x=x,
        center_y=y,
        color=(0,0,255),
        radius=60
    )

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 800, height = 600, title = 'Рисование фигур')
        self.set_background_color = (255, 255, 255)

    def on_draw(self):
        self.clear()
        for i in range(1, 4):
            create_cloud(100 * i, 400)
        for j in range(1, 3):
            create_cloud(100 * j + 50, 470)

if __name__ =='__main__':
    game = Game()
    arcade.run()

# arcade.draw_arc_outline(
#     center_x=400,
#     center_y=300,
#     width=155,
#     height=155,
#     color=(0,0,0,125),
#     start_angle=0,
#     end_angle=90,
#     tilt_angle=15,
#     num_segments=15,
#     border_width=2
# )

# arcade.draw_circle_filled(
#     center_x=400,
#     center_y=300,
#     radius=100,
#     color=(0,0,0),
#     tilt_angle=0,
#     num_segments=-1
# )

# arcade.draw_circle_outline(
#     center_x=400,
#     center_y=300,
#     radius=100,
#     color=(0,0,0),
#     tilt_angle=0,
#     num_segments=-1,
#     border_width=2
# )

# arcade.draw_ellipse_filled(
#     center_x=400,

# )