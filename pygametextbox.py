
class Textbox:
    def __init__(self, pos, font, base_color, hovering_color, text_color, size, text = ''):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_color = text_color
        self.width = size[0]
        self.height = size[1]
        self.text = text
        self.rect = self.rect(self.x_pos, self.y_pos, self.width, self.height)
        self.txt_surface = self.font.render(self.text, True, self.text_color)
        self.active = False

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def update(self):
        self.width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = self.width
