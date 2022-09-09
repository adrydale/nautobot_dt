from nautobot.extras.jobs import Job, StringVar, IntegerVar, BooleanVar
from nautobot.extras.jobs import ChoiceVar

class FirstTestJob(Job):
  var_text = StringVar(
    default = "Default value",
    description = "Test text value to be outputted to the JobResults",
    label = "Test text"
  )
  var_sleep = IntegerVar(
    default = 0,
    description = "Seconds to sleep as a test."
    label = "Sleep seconds"
  )
  var_bool = BooleanVar(
    default = True,
    description = "True/False test",
    label = "Boolean test"
  )
  var_choice = ChoiceVar(
    description = "Choice selection test",
    label = "Opportunities",
    choices = (("10","The wrong choice"),("20","The right choice"))
  )

  def Meta():
    name = "First test job"
    description = """
      This is the first test job written.
      The variables inputting will be outputted or processed
    """
    field_order = ["var_text","var_sleep","var_choice","var_bool"]

  def run(self, data, commit):
    self.log("Job start")
    self.log_debug("Degbugging log")
    self.log_success("Success log")
    self.log(f"Input - Text var: {var_text}")
    self.log(f"Sleeping for {var_sleep} seconds.")
    self.log_success("Done!")
    if var_bool:
      self.log_success("Boolean var was True!")
    else:
      self.log_failure("Boolean var was False!")
    if var_choice == "10":
      self.log_warning(f"Warning: Poor VLAN choice: {var_choice}")
    else:
      self.log_success(f"Success: Good VLAN choice: {var_choice}")
    self.log("Job complete")

  def test_02():
    msg = "Test02 function run"
    self.log(msg)
    self.log_debug(msg)

  def test_01():
    msg = "Test01 function run"
    self.log(msg)
    self.log_debug(msg)

  def post_run():
    self.log("Post run func."
