The script generate_bdq_qrg.py generates an alternate html rendering of the Quick Reference Guide (QRG) for the Biodiversity Data Quality (BDQ) draft standard. 

Copies are placed at tg2/\_review/docs/terms/bdqterms/index.html and /terms/bdqterms/index.html in the tg2 repository.  The jekyll build system used by github does not support directories starting with an underscore, so the copy in /terms/bdqterms/index.html is visible on the github pages site, but the copy in tg2/_review/docs/terms/bdqterms/index.html is not, and is only visible as a source html document in the tg2 repository.
