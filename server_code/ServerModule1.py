import anvil.server
from calendar import Calendar

@anvil.server.callable
def get_days(month):
  cal = Calendar()
  return list(cal.itermonthdates(2025, month))
