# Importing Job from nautobot.extras.jobs is required for any Nautobot job.
from nautobot.extras.jobs import Job

# These imports are the type of inputs that are being used in this job.
from nautobot.extras.jobs import StringVar, ObjectVar

# Importing models allow us to work with/manipulate objects of these types
from nautobot.dcim.models import Site
from nautobot.extras.models import Status

# This is the job grouping within the Nautobot UI.
name = "AD Example jobs"

# This is the job being imported.
class Ex05_CreatingSiteObjects(Job):
  site_name = StringVar(
    default = "Nautobot Examples - Example Site",
    description = "Name of the site to be created",
    label = "Site Name"
  )

  site_status = ObjectVar(
    #default = "Active",
    description = "Set the configured status of the site",
    label = "Site status",
    model = Status,
    query_params = {"content_types": [Site]},
    display_field = "name"
  )

  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 05 - Creating Site Objects"
    # The first line of the description will be displayed but other lines will
    #   only be displayed on job details.
    description = """
      This job will create a base site with the user inputted name.
    """

  # This will be run when the job starts.
  def run(self, data, commit):
    # Basic log
    self.log_info("Job start")

    site_name = data.get("site_name")
    site_status = data.get("site_status")
    self.log_debug(f"Site name: {site_name}")
    slef.log_debug(f"Site status: {site_status}")
