# Sphinx Demo

In this demo, we will showcase an example of how to use [sphinx](https://www.sphinx-doc.org/en/master/).

To make sure you have everything for this demo, run the following on your environment in __Windows__:

```shell
conda install sphinx sphinx_rtd_theme make
```

If you are running __Linux__ or __MAC OS__ you will not need to install ```make```.

---

## The steps

In your project directory create a directory called ```docs``` and move into it:

```shell
mkdir docs
cd docs
```

Start sphinx:

```shell
sphinx-quickstart
```

You will be prompted with several questions. Do not separate ```source``` and ```build``` directories (choose [n] on first prompt).

Give your project a fancy name.

Give it the names of the authors.

And a fancy release number.

Leave the language as [en].

You now have the initial structure for your project in the ```docs``` directory. At this point, sphinx needs to know where your project is. To do so, edit ```conf.py```.

Uncomment the following:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../DIRNAME'))
```

Remember to put the relative path to where your code is. Edit ```index.rst``` and add ```modules``` to the contents. With this, sphinx knows your project is modular and there might be some dependencies between your code units. Now that we configured sphinx, we need to tell its api we have the code all setup.

```shell
sphinx-apidoc -o . ../DIRNAME
```

With ```-o .```, sphinx is being told to output content into the current directory. With ```..```, you tell where the building blocs are. Change them accordingly. It is finally time to build your webpage!

```shell
make html
```

That's some warning messages... But the code still runs. The webpage for sphinx is in ```_build/html/index.html```. Open it with a browser if you are in Windows. Jupyter-lab is capable of properly rendering html in Linux. You may also notice there's no documentation on the site. We need to edit ```conf.py``` a little bit more. Open it and perform the next steps.

First add 'sphinx.ext.napoleon' to extensions:

```python
extensions = [
    'sphinx.ext.napoleon'
    ]
```

The [napoleon extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) allows sphinx to parse numpy and Google style docstrings, like the ones we have been using so far. Next, tell sphinx to ignore ipynb checkpoints.

```python
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.ipynb_checkpoints']
```

Now sphinx will ignore checkpoint directories. Finally, an aestetic change:

```python
html_theme = 'sphinx_rtd_theme'
```

Build the html all over again:

```shell
make html
```

And check the output of your ```index.html``` file. If you could deploy your directory you would be all set by now.

There are some services such as [Read the Docs](https://readthedocs.org/) that would allow hosting for your just developed code. In a company environment you could host it in an internal server for your colleagues to browse.

Whatever the solution, by correctly documenting your code, you remove the overhead of writing documentation on a separate instance, such as a Confluence page, for example.
