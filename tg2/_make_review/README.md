Scripts to copy updated authoritative artifacts from the tdwg/bdq/ tree into the tdwg/bdq/_review directory to run build scripts and for the submission of the standard for review.

WARNING: All files listed in the copy_files.sh script MUST NOT be edited in their destination files in the _review directory.  Current authoritative and maintained copies live elsewhere.

**copy_files.sh**  Copies authoritative files from outside the _review tree into their target locations in the _review tree.

**do_build.sh** Executes the python scripts in `_build_review/` to build artifacts from the templates, configuration files, and vocabulary documents in the `_build_review/` tree.

Third party Python libraries required by the scripts:
```
pandas
pyyaml
rdflib
```