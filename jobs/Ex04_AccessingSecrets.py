from nautobot.extras.jobs import Job
from nautobot.extras.jobs import BooleanVar

# These imports are the type of inputs that are being used in this job.
from nautobot.extras.models.secrets import Secret

# This is the job grouping within the Nautobot UI.
name = "AD Example jobs"

# This is the job being imported.
class Ex04_AccessingSecrets(Job):
  var_display_secret = BooleanVar(
    default = False,
    description = """
      Display the example secret in the job result/output. It is NOT recommended
      to do this for any actual secret. Job result data is stored and accessable
      to authorized users in plain text.

      Secrets were added in Nautobot version 1.2.0.
    """,
    label = "Display example shhh"
  )

  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 04 - Accessing Secrets"
    # The first line of the description will be displayed but other lines will
    # only be displayed on job details.
    description = """
      This example shows how to access Nautobot secrets.

      It is assumed that the Nautobot secret "example_secret_01" is already
      setup within Nautobot. Please refer to the Nautobot documentation for
      details on how to add a secret.

      https://nautobot.readthedocs.io/en/stable/core-functionality/secrets/
    """

  def run(self, data, commit):
    # This job shows how to access Nautobot secrets.

    self.log_info("Job start")
    secret = Secret.objects.get(slug="example_secret_01")
    val = secret.get_value()
    self.log_success(f"The value is {val}")
