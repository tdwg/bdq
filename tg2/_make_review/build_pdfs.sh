#!/bin/bash
# Build PDF copies of standard documents from generated Markdown files.

#pandoc --pdf-engine=pdflatex --toc --toc-depth=2 --resource-path=../_review/docs/intro/ -V geometry:margin=0.5in ../_review/docs/intro/index.md -o intro.pdf
pandoc --pdf-engine=pdfroff --toc --toc-depth=2 --resource-path=../_review/docs/guide/bdqffdq/ -V geometry:margin=0.5in ../_review/docs/bdqffdq/index.md -o bdqffdq_landing.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=1 -V geometry:margin=0.5in ../_review/docs/bdqtest/index.md -o bdqtest.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=1 -V geometry:margin=0.5in ../_review/docs/extension/bdqffdq/index.md -o bdqffdq_extension.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=2 --resource-path=../_review/docs/guide/bdqffdq/ -V geometry:margin=0.5in ../_review/docs/guide/bdqffdq/index.md -o bdqffdq_guide.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=1 -V geometry:margin=0.5in ../_review/docs/guide/implementers/index.md -o implementers_guide.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=1 -V geometry:margin=0.5in ../_review/docs/guide/synthetic/index.md -o synthetic_guide.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=1 -V geometry:margin=0.5in ../_review/docs/guide/users/index.md -o users_guide.pdf
pandoc --pdf-engine=pdflatex --toc --toc-depth=1 -V geometry:margin=0.5in ../_review/docs/terms/bdqtest/index.md -o test_quick_reference_guide.pdf
