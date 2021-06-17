# Airbrush

## Introduction

Airbrush is an interface data specification for defining a new fixed income security.

Airbrush determines the minimum set of data requirements to process a new issuance and proposes a standard naming convention for all parameters.
Using the Airbrush specification replaces the need for multiple bilateral interfaces between market participants. Internal systems and databases do not need to be re-architected, and technology providers can use their own markup languages.

Airbrush ensures that when communicating with one another, systems will send and receive the necessary set of parameters in a consistent format.

Airbrush v1 was constructed by aligning the requirements of multiple market participants including Clearstream, the Luxembourg Stock Exchange and major paying agents.

The enclosed .yaml file leverages the OpenApi Specification, enabling consumers to import the Airbrush data specification and generate a client in over 40 different languages including Java, Python and Scala.

The Origin platform publishes all trade data according to Airbrush, more information can be found on the Orign API documentation page at: https://login2.originmarkets.com/api/trades/

Please contact airbrush@originmarkets.com if you have any questions or feedback.

## Trying out the Origin Termsheet

### Installation

Start by installing [python](https://www.python.org/downloads/) onto your computer as the command line
tool to try out Airbrush is written in python. To make sure that this has worked, open a terminal program
and run:

```sh
$ python -V
Python 3.x.x
```

You should see an output as above with each `x` being a specific number depedning on the version of python
that you downloaded. Once python is installed, download the project dependencies with the following
command:

```sh
$ pip install requirements.txt
```

This should download all the requirements you need to run the command line tool. You are now ready to use
the tool.

### Usage

To make it easy to test out Origin's termsheet template, we have created a few example trades that you can
try out. You can find these in the [Examples folder](./examples/). You willd find both an
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
