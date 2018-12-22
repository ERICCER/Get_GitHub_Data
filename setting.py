import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS
def my_config(self, pygal.Config):
    #self. = pygal.Config()
    self.x_label_rotation = 45
    self.show_legend = False
    self.title_font_size = 24
    self.labels_font_size = 14
    self.major_label_font_size = 18
    self.truncate_label = 45
    self.show_y_guides = False
    self.width = 1000