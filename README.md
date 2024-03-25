# download_hmp_data

This simple script aims to download data from [HMP portal](https://portal.hmpdacc.org/search/s?facetTab=cases). Although the presence of tools to download data from this website like [HMP client](https://github.com/michbur/hmp_client) or [portal client](https://github.com/IGS/portal_client), they do not work with me for some files. So, I made this simple script to work around it. And you can use "only" it in case the main tools do not work with you.

## Usage

First, after you get your [manifest file](https://portal.hmpdacc.org/search/s?facetTab=cases), put it in the same directory of the script and run this python3 script.

```python
python3 download_urls.py -i example_manifest.tsv

```
As dependencies, you need to have (via pip3 or conda)
pandas , agrpase and wget
## Contributing
Everything is clear, right? But anyhow, contact me here or directly via email: drahmedsherbini@yahoo.com
## License
This tool aims to help others. Kindly, cite my GitHub page!
