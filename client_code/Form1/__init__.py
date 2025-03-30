from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import datetime
import time

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
    self.month = datetime.datetime.now().month
    self.now = time.localtime()
    
    self.init_components(**properties)
    
    self.label_1.text = self.month_name()
    self.label_2.text = self.week_number()
    self.button_1.set_event_handler('click', self.add_week)
    self.button_2.set_event_handler('click', self.remove_week)
    # Any code you write here will run before the form opens.   
  def setup_calendar(self):
    print("knse")
    
  def month_name(self):
    return NUMBER_TO_MONTH[self.month]
    
  def week_number(self):
    week_num = int(time.strftime("%W")) + 1 
    return "Week " + str(week_num)
  
  def add_week(self, **event_args):
    """Decrement the month"""
    print("jk")
    self.month = (self.month - 2) % 12 + 1
    self.refresh_data_bindings()
    self.setup_calendar()

  def remove_week(self, **event_args):
    """Increment the month"""
    print("kjnd")
    self.month = self.month % 12 + 1
    self.refresh_data_bindings()
    self.setup_calendar()