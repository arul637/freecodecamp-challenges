Given a string, return its camel case version using the following rules:

- Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
- The first word should be all lowercase.
- Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
- All spaces and separators should be removed.

## Examples 

```
to_camel_case("HELLO WORLD") should return "helloWorld"
to_camel_case("secret agent-X") should return "secretAgentX"
to_camel_case("FREE cODE cAMP") should return "freeCodeCamp"
o_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk") should return "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk"
```
