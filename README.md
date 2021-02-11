# Airbrush
Airbrush is an interface data specification for defining a new fixed income security.

Airbrush determines the minimum set of data requirements to process a new issuance and proposes a standard naming convention for all parameters.
Using the Airbrush specification replaces the need for multiple bilateral interfaces between market participants. Internal systems and databases do not need to be re-architected, and technology providers can use their own markup languages.

Airbrush ensures that when communicating with one another, systems will send and receive the necessary set of parameters in a consistent format.

Airbrush v1 was constructed by aligning the requirements of multiple market participants including Clearstream, the Luxembourg Stock Exchange and major paying agents.

The enclosed .yaml file leverages the OpenApi Specification, enabling consumers to import the Airbrush data specification and generate a client in over 40 different languages including Java, Python and Scala.

The Origin platform publishes all trade data according to Airbrush, more information can be found on the Orign API documentation page at: http://login2.originmarkets.com/api/trades/

Please contact airbrush@originmarkets.com if you have any questions or feedback.
