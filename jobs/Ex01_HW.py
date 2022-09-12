from nautobot.extras.jobs import Job

# This is the job grouping within the Nautobot UI.
name = "Example jobs"

# This is the job being imported.
class Ex01_HelloWorld(Job):
  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 01 - Hello World"
    # The first line of the description will be displayed but other lines will
    # only be displayed on job details.
    description = """
      Example job for a simple "Hello World" output
    """

  def run(self, data, commit):
    # This is a simple job that outputs "Hello world" to the job output/result
    # data.
    self.log("Hello world!")
