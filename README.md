# simple-json2html
A simple JSON to HTML converter in Python that utilizes recursion to grab JSON info and build an HTML table.
Uses Python's json library to convert json data to Python data structures, then converts python data structures into HTML code with proper tags to build a nested table.

There are other JSON to HTML converters out there, why is this one special?
  - The only other Python wrappers for this kind of conversion use OrderedDict, which causes many issues on different envirnoments and configurations, especially when you try to use "object_pairs_hook".
  - The code is SHORT and CLEAN. The entire conversion process is just a simple recursive function that builds a simple HTML table from Python data structures.

