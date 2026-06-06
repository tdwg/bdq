## Site build resources

Files used in the workflow build of the BDQ web pages for deployment on bdq.tdwg.org through the .github/workflows/pages.yml workflow.

These apply to the BDQ Interest Group, its Task Groups, and the BDQ (draft) standard.

├── assets
│   ├── site.css
│   ├── TDWG-Logo_horizontal-white.svg  deployed into /assets/img/
│   ├── tdwg-logo-short.svg deployed into /assets/img/
│   └── toc.js
├── __init__.py
├── README.md  this file
├── render_site_links.py  library of functions to render links in the site pages, used by render_site.py
├── render_site.py  script to render the site pages, using the functions in render_site_links.py invoked in the .github/workflows/pages.yml workflow
├── templates
│   └── page.html  template for the site pages, used by render_site.py
└── tests
    └── test_render_site_links.py unit tests for the functions in render_site_links.py


## Unit Tests

Execute from the root of the bdq repository with:

```
python -m pytest _site_resources/tests/test_render_site_links.py
```
