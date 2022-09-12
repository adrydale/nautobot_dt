# Importing Job from nautobot.extras.jobs is required for any Nautobot job.
from nautobot.extras.jobs import Job
from nautobot.extras.jobs import BooleanVar

# This is the job grouping within the Nautobot UI.
name = "Example jobs"

# This is the job being imported.
class Ex03_TestAndPostRunFunctions(Job):
  # This example demonstrates the test_*() and post_run() functions. These are
  # run after the run() function in order to validate data/objects/state and
  # complete clean-ups or other efforts in the event that the run() function
  # fails.

  # This boolean var is used to raise an exception within the fun() function to
  # show that the test_*() and post_run() functions are still processed.
  var_induce_failure = BooleanVar(
    default = False,
    description = "Check this to induce a job failure/exception",
    label = "Create exception in run()"
  )

  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 03 - Test and post-run functions"
    # The first line of the description will be displayed but other lines will
    #   only be displayed on job details.
    description = """
      Demonstrate the test_*() and post_run() functions.

      These functions are run after the run() function in order to validate the
      data/objects/state and complete clean-ups or other efforts in the event 
      that the run() function
    """

  def run(self, data, commit):
    self.log("Job start")

    induce_failure = data.get('var_induce_failure')
    self.log(f"Checkbox to induce a failure was set to {induce_failure}")
    if induce_failure:
      raise ValueError("User requested to induce a failure (intentional).")

  # All test_* functions will be implicitly called *after* the run() function.
  # These are processed in the order they are defined.
  # test_ functions are OPTIONAL
  def test_02(self):
    msg = "Test02 function run"
    self.log(msg)

  def test_01(self):
    msg = "Test01 function run"
    self.log_debug(msg)

  # Finally, the post_run() will always run after the run() and test_*()
  # functions are run regardless of any failures. This method can be used to
  # ensure clean-ups are completed in all cases.
  def post_run(self):
    self.log("Post run func.")
