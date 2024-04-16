# download_hmp_data

This simple script aims to download data from [HMP portal](https://portal.hmpdacc.org/search/s?facetTab=cases). Although the presence of tools to download data from this website like [HMP client](https://github.com/michbur/hmp_client) or [portal client](https://github.com/IGS/portal_client), they do not work with me for some files. So, I made this simple script to work around it. And you can use it in case the main tools do not work with you.

**Note**: This script supports only valid HTTPS (not Amazon s3, FTP clients) 

## Usage

First, after you get your [manifest file](https://portal.hmpdacc.org/search/s?facetTab=cases), put it in the same directory of the script and run this python3 script.

```python
python3 download_urls.py -i example_manifest.tsv

```
As dependencies, you need to have (via pip3 or conda)
pandas , agrpase and get

**To examine some current manifest HTTPS validity, you have two options.**

Randomly pick a few of them.

1- Manually, on the website itself like in [example](https://portal.hmpdacc.org/files/91319e642fdd8a6e3b059cfb05915bde), try the manual download button per individual file, if it works, a good sign.

2- From your TSV file copy and paste the link (https://.............bz2) in your browser, if you can see be downloaded, then this is a good sign.

As an output, your manifest will be divided into one successful manifest and one failed manifest file (to list the samples that were not downloaded).

## Contributing
Everything is clear, right? But anyhow, contact me here or directly via email: drahmedsherbini@yahoo.com
## License
This tool aims to help others. Kindly, cite my GitHub page!
