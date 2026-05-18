from ._anvil_designer import ListUsersTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .. import Global
from .. import FunctionsB

class ListUsers(ListUsersTemplate):
  #def list_users_refresh(self, **event_args):
  #  # this function does the filling of the table contents
  #  self.UsersList.items = anvil.server.call('users_get')
  #  self.table.rows_per_page = Global.rows_per_page
  #  self.total_user_number.text = "Total number of Users: " + str(len(self.UsersList.items))
  #pass
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    #print("in ListUsers")
    #Global.help_page.visible = False
    #Global.header.visible = False
    Global.main_form.menu_bottom.visible = True
    #Global.main_form.mb_left.visible = False
    #Global.main_form.mb_middle.visible = False
    #Global.main_form.refresh.visible = True
    #
    # save self in Global.work_area
    Global.work_area[Global.current_work_area_name]["self"] = self
    
    # Set table role to horizontal scroll
    self.table.role = "horizontal-scroll"
    
    #self.list_users_refresh()
    FunctionsB.list_users_refresh(self)



