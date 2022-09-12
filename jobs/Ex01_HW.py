from nautobot.extras.jobs import Job

name = "Example jobs"

class Ex01_HelloWorld(Job):
  def Meta():
    name = "Example 01 - Hello World"
    description = """
      Example job for a simple "Hello World" output
    """
  def run(self, data, commit):
    self.log("Hello world!")
