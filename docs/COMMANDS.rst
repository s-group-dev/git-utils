GUTS Command Reference
======================

$ guts branch list-merged
-------------------------

   List all other branches that are merged to given branch.

::

   Usage: guts.py branch list-merged [OPTIONS]
   
     List all other branches that are merged to given branch.
   
   Options:
     -b, --branch TEXT  Default branch/trunk
     -r, --remote TEXT  Remote to check against. If omited, checks against local
     -f, --filter TEXT  Filter output (case-insensitive)
     --delete           Delete merged branches
     --help             Show this message and exit.

$ guts branch list-wip
----------------------

   List all other branches that are NOT merged to given branch.

::

   Usage: guts.py branch list-wip [OPTIONS]
   
     List all other branches that are NOT merged to given branch.
   
   Options:
     -b, --branch TEXT  Default branch/trunk
     -r, --remote TEXT  Remote to check against. If omited, checks against local
     -f, --filter TEXT  Filter output (case-insensitive)
     --delete           Delete merged branches
     --help             Show this message and exit.

$ guts remote merge-subtree
---------------------------

   Merge given remote to local branch.

::

   Usage: guts.py remote merge-subtree [OPTIONS]
   
     Merge given remote to local branch.
   
   Options:
     -r, --remote TEXT  Absolute URL pointing to a project.  [required]
     -b, --branch TEXT  Default branch/trunk
     -t, --target TEXT  Target directory.
     --help             Show this message and exit.

$ guts repository clean-up
--------------------------

   Clean up repository and reduce its disk size.

::

   Usage: guts.py repository clean-up [OPTIONS]
   
     Clean up repository and reduce its disk size.
   
   Options:
     --help  Show this message and exit.

