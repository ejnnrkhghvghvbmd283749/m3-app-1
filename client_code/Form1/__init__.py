# add the notes panel, and three buttons 

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
    self.background = "#DAFFCB"
    self.column_panel_1.background="#D7DBD3"
    self.column_panel_1.role = "radius-round"
    self.current = datetime.datetime.now()
    self.month = self.current.month
  
    self.week_num = int(self.current.strftime("%W")) + 1
    self.label_2.text = self.week_number()
    self.week_names()
    self.week_dates()
    
    self.button_1.set_event_handler('click', self.add_week)
    self.button_2.set_event_handler('click', self.remove_week)   
  def month_name(self):
    return NUMBER_TO_MONTH[self.month]
    
  def week_number(self):
    return "Week " + str(self.week_num)

  def week_names(self):
    self.flow_panel_1.clear()
    start_of_week = self.current - datetime.timedelta(days=self.current.weekday())
    self.flow_panel_1.role = "pad-panel"
    for i in range(7):
      week_name = start_of_week + datetime.timedelta(days=i)
      formatted = week_name.strftime("%A")
      label = Label(text = formatted, background = "", width="80", align="center")
      self.flow_panel_1.add_component(label, expand="3")
   
  def week_dates(self):
    self.flow_panel_2.clear()
    self.flow_panel_3.clear()
    start_of_week = self.current - datetime.timedelta(days=self.current.weekday())
    self.flow_panel_3.role = "padded-panel"
    self.flow_panel_2.role = "padd-panel"
    for i in range(7):
      day_date = start_of_week + datetime.timedelta(days=i)
      formatted = day_date.strftime("%d.%m")
      label = Label(text = formatted, background = "", width="80", align="center")
      #label1 = Label(text ="", background = "white", width="120", align="center")
      text = TextArea(background="white", height="450", align=self.flow_panel_2, margin="15")
      self.flow_panel_3.add_component(text, expand="1")
      self.flow_panel_2.add_component(label, expand="3")
    
    
  def add_week(self, **event_args):
    self.current += datetime.timedelta(weeks=1)
    self.week_num = int(self.current.strftime("%W")) + 1
    self.label_2.text = self.week_number()
    self.week_names()
    self.week_dates()

  def remove_week(self, **event_args):
    self.current -= datetime.timedelta(weeks=1)
    self.week_num = int(self.current.strftime("%W")) + 1
    self.label_2.text = self.week_number()
    self.week_names()
    self.week_dates()
    