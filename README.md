Gemini Template for Pelican
============================

**Author:** [Thransoft](https://soft.thran.uk).

**Licence:** MIT

**Authored:** 21/11/2021

A simple template for a simple markup language. Currently supports rendering of basic pages linked from your homepage. Pending support for categories, tags, etc.

Still not ready for the real world.

## Usage

Requires slight tweaking of your Pelicanconf. A sample has been provided.

Output files are Gemtext-compliant and may be dumped anywhere.

It is possible to invoke Pelican with any `pelicanconf.py` file, so it is intended that this template could be used to generate both HTML and Gemtext versions of your website.

Run: `pelican -s pelicanconf_gemini.py` 

## Potential bugs

Since Pelican is intended to generate HTML, there is a strong chance some HTML markup might sneak into the output.

## known bugs

- I can't confugure pelican to stop generating certain pages, like article tag lists.
- I can't disable tags or other unwanted pages. These are output as HTML which is invalid Gemtext.
- I call striptags to remove HTML markup, but this dosen't preserve spaces or any formatting from the source files.

I know from the Jinja site it is possible to configure output syntax, (i.e. Gemtext style links, headings, links)  but I haven't yet seen how.

## Quirks

Numerous empty files (eg, archives.gmi, tags.gmi) exist. This is to stop Pelican complaining that the files can't be found. A more elegant solution would be to disable them.
