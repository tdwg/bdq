Scripts to copy updated authoritative artifacts from the tdwg/bdq/ tree into the tdwg/bdq/_review directory to run build scripts and for the submission of the standard for review.

WARNING: All files listed in the copy_files.sh script MUST NOT be edited in place in the _review directory.  Current authoriative and maintained copies live elsewhere.

copy_files.sh  Copies authoritative files from outside the _review tree into their target locations in the _review tree.

do_build.sh Executes the python scripts in _review/build/ to build artifacts from the templates, configuration files, and vocabulary documents in the _review tree.

Third party Python libraries required by the scripts:
```
pandas
pyyaml
rdflib
```