# Cookiecutter CompBio

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for computational biology projects.

This uses cookiecutter to create a repository with a similar structure to what was described in [A Quick Guide to Organizing Computational Biology Projects](https://doi.org/10.1371/journal.pcbi.1000424) by 
William Stafford Noble, while also implementing some additional best practices, such as code styling (With black or r-styler) and data-versioning/pipelining (With [DVC](https://dvc.org/)).

It's still very much a work-in-progress, If you have any ideas or contributions, feel free to post an issue or send a pull request.

# Quickstart

* Install cookiecutter

`pip install -U cookiecutter`

Or:

`conda install -c conda-forge cookiecutter`

* Initialize the project

`cookiecutter https://github.com/jvfe/cookiecutter-compbio.git`

* Create the enviroment and start working!

`conda env create --file environment.yml`

# References

Noble WS (2009) A Quick Guide to Organizing Computational Biology Projects. PLOS Computational Biology 5(7): e1000424. https://doi.org/10.1371/journal.pcbi.1000424
