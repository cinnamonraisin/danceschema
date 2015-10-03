danceschema
===========
DanceSchema is JSON schema specification for the exchange of Structured "Traditional" Dances.

We provide:
* A formal JSON schema for generic structured dances.
* Error detection and validation for dances. (TODO)
* Python APIs for parsing text from other formats into the StructuredDance format.

Dances forms which might be encompassed by this format include, but are not limited to:
* Contra Dances
* Square Dances
* English Country Dances
* Scottish Country Dances

Goals
-----
We are offering this open source in an effort to encourage contribution from the community.
We are extremely aware that there are many people out there in the world who have thought about
storing traditional dances in databases, and serving them on the web. Our objective of this project
is to facilitate the digital interchange of these dances for the benefit of the greater traditional
dance community.

Contributing
------------
To that end, we welcome pull requests to this document to generally improve the format.
Contributions are especially welcome in the following areas:
* Suggestions and observations about how to keep our format general, yet powerful.
* Additional APIs for processing valid StructuredDance files in different languages. We'll start a python version, but we would welcome other people to provide them for other languages.

What This Is Not
----------------
This repository is not a place to include your dances. That's what a database is for. The "examples" folder should have a collection of dances from each of the main categories which contain a variety of different problems which might be solved by this format.
