# bayes
Static website for a study group for John Kruschke's Doing Bayesian Data analysis, 2nd edition

## Installation
Development for the site is done on the `dev` branch, and published through the `master` branch.

    git clone https://github.com/leblancfg/bayes
    cd bayes
    git checkout dev

### Pelican
The site uses a [static site generator called Pelican](https://blog.getpelican.com/). The content for the pages can be found in the `content` folder.

To install pelican and requirements:
    pip install pelican ghp-import

### Github Pages
The site is hosted on Github Pages. See [setting up Github Pages](https://guides.github.com/features/pages/).

## Build
Once installed, building the website should be as simple as

    make github
