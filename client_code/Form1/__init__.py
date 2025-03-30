from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import datetime
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

    self.current = datetime.datetime.now()
    self.month = self.current.month
    
    self.week_num = int(self.current.strftime("%W")) + 1
    self.label_2.text = self.week_number()
    
    self.button_1.set_event_handler('click', self.add_week)
    self.button_2.set_event_handler('click', self.remove_week)   
  def month_name(self):
    return NUMBER_TO_MONTH[self.month]
    
  def week_number(self):
    return "Week " + str(self.week_num)
  
  def add_week(self, **event_args):
    self.current += datetime.timedelta(weeks=1)
    self.week_num = int(self.current.strftime("%W")) + 1
    self.label_2.text = self.week_number()

  def remove_week(self, **event_args):
    self.current -= datetime.timedelta(weeks=1)
    self.week_num = int(self.current.strftime("%W")) + 1
    self.label_2.text = self.week_number()