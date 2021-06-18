# Airbrush

## Introduction

Airbrush is an interface data specification for defining a new fixed income security.

Airbrush determines the minimum set of data requirements to process a new issuance and proposes a standard
naming convention for all parameters. Using the Airbrush specification replaces the need for multiple
bilateral interfaces between market participants. Internal systems and databases do not need to be
re-architected, and technology providers can use their own markup languages.

Airbrush ensures that when communicating with one another, systems will send and receive the necessary
set of parameters in a consistent format.

Airbrush v1 was constructed by aligning the requirements of multiple market participants including
Clearstream, the Luxembourg Stock Exchange and major paying agents. In Airbrush v2, we have continued
to work closely with industry participants to extend the scope of communication that the data specification
can support to:

 1. Termsheet Stage: For requesting ISINs and other identifiers or communicating about a completed trade

 2. Post-Trade Stage: For communicating with clearing systems, listing exchanges, paying agents and other
 market participants

## Getting Involved

This Github repo contains a number of useful resources and tools for anyone interesting in seeing how
Airbrush works and using it within their own systems. The Origin Documentation product is built on the same
tools and we hope that by sharing them, we can encourage stronger collaboration and standardisation across
the market.

 1. [Airbrush OpenAPI Specification](<Airbrush v1.0.yaml>): The Airbrush data specification defined in a
 yaml file that leverages the [OpenApi](https://www.openapis.org/) Specification, enabling consumers to
 import the data specification and generate a client in over 40 different languages including Java, Python
 and Scala. The Origin platform publishes all trade data according to Airbrush; more information can be
 found on the [Orign API documentation page](https://login2.originmarkets.com/api/trades/).

 2. [Machine-Readable Termsheet Template](<Machine-Readable Termsheet.docx>): A machine-readable termsheet
 template created using the [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) templating language. This
 template is open-source and free to use by all fixed-income market participants to foster
 standardisation of bond issuance documents.

 3. [Standardised Termsheet Template](<Standardised Termsheet.docx>): An equivalent version of the
 machine-readable template for easier reading.

 4. [Example Airbrush Outputs](./examples): A number of example issuances represented in the Airbrush
 data format.

 5. [Command Line Tool](create_termsheet.py) for Creating New Termsheets from Airbrush data: This simple
 command line tool serves as example python code that can be used to generate a new termsheet based on
 the Machine-Readable Termsheet Template and an Airbrush-compliant data file. Please see the [instructions
 below](#termsheet-creator-command-line-tool) to try it out.

If you want to learn more about Airbrush and Origin, or have any feedback, send us an email at
airbrush@originmarkets.com.

## Termsheet Creator Command Line Tool

The python command line tool can be used to create a new termsheet based on the
[Machine-Readable Termsheet Template]("Machine-Readable Termsheet.docx") and an Airbrush-compliant JSON
file containting the data for a trade.

### Installation

Start by installing [python](https://www.python.org/downloads/) onto your computer as the command line
tool to try out Airbrush is written in python. To make sure that this has worked, open a terminal program
and run:

```sh
python -V
```

You should see an output of `Python 3.x.x` with each `x` being a specific number depending on the version
of python that you downloaded. Once python is installed, clone the repo using [git](https://git-scm.com/)
and change your working directory to the project:

```sh
git clone https://github.com/OriginMarkets/Airbrush.git
cd Airbrush
```

Create a virtual environment to install the project dependencies into and enter it:

```sh
python -m venv venv
source venv/bin/activate
```

Now that the repo is downloaded, get the project dependencies with the following
[pip](https://www.python.org/downloads/) commands:

```sh
pip install --upgrade pip
pip install -r requirements.txt
```

This should download all the requirements you need to run the command line tool. You are now ready to use
the tool.

### Usage

```
usage: python create_termsheet.py [-h] json_input_file docx_output_file

A command line tool to create a termsheet using the Origin termsheet template with an Airbrush-compliant json file

positional arguments:
    json_input_file   The path to the json input file
    docx_output_file  The path to create the docx termsheet at

optional arguments:
    -h, --help        show this help message and exit
```

To make it easy to test out Origin's termsheet template, we have created a few example trades that you can
try out. You can find these in the [Examples folder](./examples). You will find both an
Airbrush-compliant json input file and a docx output file for the following trade types.

To see this tool in action, you can now run the following command in your terminal to create your own
termsheet based on a json input file:

```sh
python create_termsheet.py examples/fixed_rate.json examples/fixed_rate.docx
```

Feel free to update or create a new input file to see the corresponding docx file created by running the
general command in your terminal:

```sh
python create_termsheet.py examples/my_trade.json examples/my_termsheet.docx
```
