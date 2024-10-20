#!/bin/bash
# Build PDF copies of standard documents from generated markdown files.
pandoc --pdf-engine=pdflatex --toc --toc-depth=2 --resource-path=../_review/docs/intro/ -V geometry:margin=0.5in ../_review/docs/intro/index.md -o intro.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=1 -V geometry:margin=0.5in ../_review/docs/guide/users/index.md -o users_guide.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=1 -V geometry:margin=0.5in ../_review/docs/terms/bdqcore/index.md -o test_quick_reference_guide.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=2 --resource-path=../_review/docs/guide/bdqffdq/ -V geometry:margin=0.5in ../_review/docs/guide/bdqffdq/index.md -o bdqffdq_guide.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=1 -V geometry:margin=0.5in ../_review/docs/guide/implementers/index.md -o implementers_guide.pdf
