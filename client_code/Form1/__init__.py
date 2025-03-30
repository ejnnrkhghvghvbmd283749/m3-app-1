from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

NUMBER_TO_MONTH = {
  1: 'January',
  2: 'February',
  3: 'March',
  4: 'April',
  5: 'May',
  6: 'June',
  7: 'July',
  8: 'August',
  9: 'September',
  10: 'October',
  11: 'November',
  12: 'December',
}

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.month = 11
    self.init_components(**properties)
    self.label_1.txt = self.month_name()
    # Any code you write here will run before the form opens.    
  def month_name(self):
    return NUMBER_TO_MONTH[self.month]
