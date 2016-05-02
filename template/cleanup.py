# delete all .pyc files.
import fileter
it = fileter.iterators.RemoveFiles(force=True)
it.add_pattern("*.pyc")
it.process_all()
